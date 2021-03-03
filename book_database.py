import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

#Forms connection to database
def getConnection():
	connection = psycopg2.connect(	database='bookdb',
									user='qfx18seu',
									password= 'Blackpanther2018!',
									host = "127.0.0.1",
									port = "5432")
	return connection
	
#Returns homepage
@app.route("/")
def index():
  return render_template("index.html")

##### LINKS TO WEBPAGES WITH FORMS#####

#Returns webpage with task 1 form
@app.route("/task-1-form")
def task1Form():
  return render_template("task-1-form.html")

#Returns webpage with task 2 form
@app.route("/task-2-form")
def task2Form():
  return render_template("task-2-form.html")

#Returns webpage with task 3 form
@app.route("/task-3-form")
def task3Form():
  return render_template("task-3-form.html")

#Returns webpage with task 4 form
@app.route("/task-4-form")
def task4Form():
  return render_template("task-4-form.html")
 
#Returns webpage with task 5 form 
@app.route("/task-5-form")
def task5Form():
  return render_template("task-5-form.html")

#Returns webpage with task 6 form 
@app.route("/task-6-form")
def task6Form():
  return render_template("task-6-form.html")

#Returns webpage with task 7 form  
@app.route("/task-7-form")
def task7Form():
  return render_template("task-7-form.html")

#####FUNCTIONS TO EXECUTE SQL QUERIES AND RETURN RESULTS (e.g. tables, reports, etc.)#####

#Executes SQL queries for task 1 form and returns result
@app.route('/category-created', methods =['POST'])
def createCategory():
	try:
		connection = None
		id = int(request.form['CategoryID'])
		name = request.form['CategoryName']
		type = request.form['CategoryType']
		
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('INSERT INTO Category VALUES (%s, %s, %s);\
						SELECT * FROM Category;', [id, name, type])
		
		rows = cursor.fetchall()
		if rows:
			return render_template('books.html', rows=rows, msg1 = 'Record added successfully.')
		else:
			return render_template('index.html', msg1 = 'Unable to view table.')
	
	except Exception as e:
		return render_template('index.html', msg1 = 'Unable to create record.', error1 = e)
	
	finally:
		if connection:
		connection.close()
  
#Executes SQL queries for task 2 form and returns result
@app.route('/category-deleted', methods =['POST'])
def deleteCategory():
	try:
		connection = None
		id = int(request.form['CategoryID'])
		
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('DELETE FROM Category WHERE CategoryID = %s;\
						SELECT * FROM Category;', [id])
		
		rows = cursor.fetchall()
		if rows:
			return render_template('categories.html', rows=rows, msg2 = 'Record deleted successfully.')
		else:
			return render_template('index.html', msg2 = 'Unable to view table.')
	
	except Exception as e:
		return render_template('index.html', msg2 = 'Unable to delete record.', error2 = e)
	
	finally:
		if connection:
		connection.close()

#Executes SQL queries for task 3 form and returns result 
@app.route('/category-summary-report', methods =['GET'])
def categoryReport():
	try:
		connection = None
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('CREATE VIEW BookSummaryReport AS\
							SELECT Book.CategoryID AS CategoryID, Category.Name AS CategoryName,\
							COUNT(Title) AS NumberOfBookTitles, AVG(Price) AS AveragePrice\
							FROM Book\
							INNER JOIN Category ON Book.CategoryID = Category.CategoryID\
							GROUP BY Book.CategoryID\
							UNION ALL\
							SELECT NULL, "Total", COUNT(Title), AVG(Price)\
							FROM Book;\
						SELECT * FROM BookSummaryReport;')
						
		rows = cursor.fetchall()
		if rows:
			return render_template('category-report.html', rows = rows, msg3 = 'Report generated successfully')
		else:
			return render_template('index.html', msg3 = 'Unable to generate report.')
			
	except Exception as e:
		return render_template('index.html', msg3 = 'Unable to generate report.', error3 = e)
	
	finally:
		if connection:
		connection.close()

#Executes SQL queries for task 4 form and returns result
@app.route('/publisher-order-report', methods =['GET'])
def publisherReport():
	try:
		connection = None
		name = request.form['PublisherName']
		
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('CREATE VIEW BookOrderReport AS\
							SELECT YEAR(OrderDate) AS Year, MONTH(OrderDate) AS Month,\
							Orderline.BookID AS BookID, Title AS BookTitle,\
							COUNT(Orderline.BookID) AS NumberOfOrders, SUM(Quantity) AS TotalQuantity,\
							SUM(UnitSellingPrice + Price) AS TotalSellingValue\
							FROM Orderline\
							INNER JOIN Book ON Orderline.BookID = Book.BookID\
							INNER JOIN Publisher ON Book.PublisherID = Publisher.PublisherID\
							INNER JOIN ShopOrder ON Orderline.ShopOrderID = ShopOrder.ShopOrderID\
							WHERE Publisher.Name = %s\
							GROUP BY YEAR(OrderDate), MONTH(OrderDate), Orderline.BookID\
							ORDER BY YEAR(OrderDate) DESC, MONTH(OrderDate) DESC;\
						SELECT*FROM BookOrderReport;', [name])
		
		rows = cursor.fetchall()
		if rows:
			return render_template('publisher-report.html', rows = rows, msg4 = 'Report generated successfully')
		else:
			return render_template('index.html', msg4 = 'Unable to generate report.')
	
	except Exception as e:
		return render_template('index.html', msg4 = 'Unable to generate report.', error4 = e)
	
	finally:
		if connection:
		connection.close() 

#Executes SQL queries for task 5 form and returns result
@app.route('/book-order-history', methods =['GET'])
def orderHistory():
	try:
		connection = None
		id = request.form['BookID']
		
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('CREATE VIEW BookOrderHistory AS\
						SELECT OrderDate, Title, ShopOrder.ShopOrderID As OrderTitle,\
						Price, UnitSellingPrice, Quantity AS TotalQuantity,\
						SUM(Price+UnitSellingPrice) AS OrderValue, Shop.Name\
						FROM Orderline\
						INNER JOIN ShopOrder ON Orderline.ShopOrderID = ShopOrder.ShopOrderID\
						INNER JOIN Book ON Orderline.BookID = Book.BookID\
						INNER JOIN Shop ON ShopOrder.ShopID = Shop.ShopID\
						WHERE Orderline.BookID = %s\
						GROUP BY OrderDate\
						UNION ALL\
						SELECT NULL, NULL, NULL, NULL, "Total", SUM(Quantity), SUM(UnitSellingPrice), NULL\
						FROM Orderline\
						WHERE Orderline.BookID = %s;\
						SELECT*FROM BookOrderHistory;', [id, id])
		
		rows = cursor.fetchall()
		if rows:
			return render_template('order-history.html', rows = rows, msg5 = 'Report generated successfully')
		else:
			return render_template('index.html', msg5 = 'Unable to generate report.')
			
	except Exception as e:
		return render_template('index.html', msg5 = 'Unable to generate report.', error5 = e)
	
	finally:
		if connection:
		connection.close()

#Executes SQL queries for task 6 form and returns result  
@app.route('/sales-rep-performance-report', methods =['GET'])
def performanceReport():
	try:
		connection = None
		date1 = request.form['StartDate']
		date2 = request.form['EndDate']
		
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('CREATE VIEW SalesRepPerformanceReport AS\
						SELECT SalesRep.SalesRepID AS SalesRepID, SalesRep.Name AS Name,\
						COUNT(Orderline.ShopOrderID) AS TotalOrders, SUM(Quantity) AS TotalUnitsSold,\
						SUM(UnitSellingPrice) AS TotalOrderValue\
						FROM SalesRep\
						INNER JOIN ShopOrder ON SalesRep.SalesRepID = ShopOrder.SalesRepID\
						INNER JOIN Orderline ON ShopOrder.ShopOrderID = Orderline.ShopOrderID\
						WHERE OrderDate BETWEEN %s AND %s\
						GROUP BY SalesRep.SalesRepID\
						ORDER BY COUNT(Orderline.ShopOrderID) DESC;\
						SELECT*FROM SalesRepPerformanceReport;', [date1, date2])
		rows = cursor.fetchall()
		if rows:
			return render_template('performance-report.html', rows = rows, msg6 = 'Report generated successfully')
		else:
			return render_template('index.html', msg6 = 'Unable to generate report.')
	
	except Exception as e:
		return render_template('index.html', msg6 = 'Unable to generate report.', error6 = e)
	
	finally:
		if connection:
		connection.close()

#Executes SQL queries for task 7 form and returns result
@app.route('/discount-applied', methods =['POST'])
def applyDiscount():
	try:
		connection = None
		id = int(request.form['CategoryID'])
		discount = int(request.form['Discount'])
		
		connection = getConnection()
		cursor = connection.cursor()
		cursor.execute('SET search_path to bookdb')
		
		cursor.execute('UPDATE Book\
						SET Price = Price - (Price*(%s/100))\
						WHERE Book.CategoryID = %s;\
						SELECT * FROM Books;', [discount, id])
		
		rows = cursor.fetchall()
		if rows:
			return render_template('books.html', rows = rows, msg7 = 'Discount applied successfully')
		else:
			return render_template('index.html', msg7 = 'Unable to generate report.')
	
	except Exception as e:
		return render_template('index.html', msg7 = 'Unable to apply discount.', error7 = e)
	
	finally:
		if connection:
		connection.close()
		
if __name__ == "__main__":
  app.run(debug = True)