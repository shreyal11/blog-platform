from flask import Flask, request, render_template
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root",
                database="blogdb"
            )
            return conn
        except:
            print("Waiting for MySQL...")
            time.sleep(5)

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        content = request.form['content']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO posts
            (title, author, category, content)
            VALUES (%s, %s, %s, %s)
            """,
            (title, author, category, content)
        )

        conn.commit()

        cursor.close()
        conn.close()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT id, title, author, category
    FROM posts
    ORDER BY id DESC
    """
)

    posts = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        posts=posts
    )
@app.route('/delete/<int:id>')
def delete_post(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM posts WHERE id = %s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return '''
    <script>
        window.location.href='/';
    </script>
    '''
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):

    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        content = request.form['content']

        cursor.execute("""
            UPDATE posts
            SET title=%s, author=%s, category=%s, content=%s
            WHERE id=%s
        """, (title, author, category, content, id))

        conn.commit()

        cursor.close()
        conn.close()

        return "<script>window.location.href='/'</script>"

    cursor.execute("SELECT * FROM posts WHERE id=%s", (id,))
    post = cursor.fetchone()

    cursor.close()
    conn.close()

    return f"""
    <h2>Edit Post</h2>

    <form method="POST">

        Title:<br>
        <input name="title" value="{post[1]}"><br><br>

        Author:<br>
        <input name="author" value="{post[2]}"><br><br>

        Category:<br>
        <input name="category" value="{post[3]}"><br><br>

        Content:<br>
        <textarea name="content">{post[4]}</textarea><br><br>

        <button type="submit">Update</button>

    </form>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
