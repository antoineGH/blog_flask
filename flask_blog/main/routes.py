from flask import render_template, request, Blueprint, flash
from flask_blog.models import Post
from flask_blog.posts.forms import SearchForm
from flask_blog import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():
    searchform = SearchForm()

    if searchform.filter.data == 'search': 
        search = searchform.search.data
        results = Post.query.whoosh_search(search).all()
        print(results)
        for result in results:
            print(result.title, result.content)
        return render_template('search.html', title="Search " + search, results=results, search=search)
     
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('home.html', posts=posts, title='Home', searchform=searchform)
