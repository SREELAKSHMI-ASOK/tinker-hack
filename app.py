from flask import Flask, render_template, request, jsonify
import mysql.connector

app=Flask(__name__)

mydb=mysql.connector.connect(host="localhost", user="root", password="SYSTEM", database="OhNoNosh")
cur=mydb.cursor()

@app.route('/')
def index():
    return render_template('restaurant.html')

@app.route('/menu')
def get_menu():
    cur.execute("SELECT * FROM menu")
    menu_items=cur.fetchall()
    menu_list=[]
    for item in menu_items:
        menu_list.append({
            'Item_Id': item[0],
            'Item_Name': item[1],
            'PRICE': item[2],
            'Item_Type': item[3]
        })
    return jsonify(menu_list)

@app.route('/order', methods=['POST'])  
def place_order():
    if request.method=='POST':
        data=request.get_json()
        item_id=data.get('itemId')
        quantity=data.get('quantity')
        name=data.get('name')
        mobno=data.get('mobno')
        address=data.get('address')

        try:
            a="select * from menu where Item_Id={}".format(item_id)
            cur.execute(a)
            a=cur.fetchall()
            b= a[0][2]
            c=quantity * b
            ins="insert into customer values('{}',{},{},{},'{}',{})".format(name, item_id, quantity, mobno, address, c)
            cur.execute(ins)
            mydb.commit()
            return jsonify({'message': 'Order placed successfully!'})
        except Exception as e:
            mydb.rollback()
            return jsonify({'error': str(e)})
        

    return jsonify({'message': 'Invalid request'})


if __name__=='__main__':
    app.run(debug=True)
