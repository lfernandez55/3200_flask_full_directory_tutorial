# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Blueprint, redirect, render_template
from flask import request, url_for


#from app import db

#after defining the car_blueprint you can use it as a decorator in your views below
car_blueprint = Blueprint('cars', __name__, template_folder='templates')


@car_blueprint.route('/baz')
def baz():
    return render_template('cars/baz.html')