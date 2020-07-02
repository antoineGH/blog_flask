from flask import render_template, request, Blueprint, redirect, url_for
from flask_blog.models import Post
from flask_blog.posts.forms import SearchForm

main = Blueprint('main', __name__)

@main.context_processor
def context_processor():
    searchform = SearchForm()
    return {'searchform': searchform}

@main.route('/search', methods=['POST'])
def search():
    searchform = SearchForm()
    if not searchform.validate_on_submit():
        return redirect(url_for('main.home'))
    return redirect(url_for('main.search_results', query=searchform.search.data))

@main.route('/search_results/<query>')
def search_results(query):
    results = Post.query.whoosh_search(query).all()
    return render_template('search.html', title="Search " + query, query=query, results=results)

@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def home():    
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template('home.html', posts=posts, title='Home')
