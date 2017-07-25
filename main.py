#-*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect

from stock_model import Stock

app = Flask(__name__)
app.secret_key = 'some_secret'
app.debug = True

@app.route(r'/marquesitas', methods=['GET'])
def contact_book():
    contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)

@app.route(r'/Paco', methods=['GET'])
def stock_list():
    stocks = Stock.query().fetch()
    return render_template('paco.html', stocks=stocks)


# return render_template('contact_book.html')
    #return 'PP Marquesitas, tradición familiar desde 1853'

@app.route(r'/marquesitas/agregar', methods=['GET','POST'])
def add_contact():
    if request.form:
         contact = Contact(name=request.form.get('name'),precio=request.form.get('precio'))
         contact.put()
         flash('¡Se añadió la marquesita!')
#  print(request.form.get('name'))
      #  print(request.form.get('phone'))
      #  print(request.form.get('email'))

    return render_template('add_contact.html')

@app.route(r'/contacts/<uid>',methods=['GET'])
def contact_details(uid):
    contact = Contact.get_by_id(int(uid))

    if not contact:
        return redirect('/marquesitas', code=301)

    return render_template('contact.html', contact=contact)

@app.route(r'/delete', methods=['POST'])
def delete_contact():
    contact = Contact.get_by_id(int(request.form.get('uid')))
    contact.key.delete()
    return redirect('/contacts/{}'.format(contact.key.id()))

@app.route(r'/legnis')
def legnis():
    return render_template('legnis.html')

@app.route(r'/Regino')
def regino():
    return render_template('regino.html')

if __name__ == '__main__':
    app.run()

