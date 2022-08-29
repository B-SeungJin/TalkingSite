from flask import Blueprint

page_ab = Blueprint('talk', __name__)

@page_ab.route('/talk1')
def talk():
    return 'TALKING PAGE'