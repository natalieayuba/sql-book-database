--  sql program to set up test data for database

SET SEARCH_PATH TO BookWholesalerDatabase;

-- populate Category table

INSERT INTO Category(CategoryID, Name, CategoryType) VALUES
    ('1', 'Romance', 'Fiction'),
    ('2', 'Fantasy', 'Fiction'),
    ('3', 'Horror', 'Fiction'),
    ('4', 'Art', 'Non-fiction'),
    ('5', 'Lifestyle', 'Non-fiction');

-- populate SalesRep table

INSERT INTO SalesRep(SalesRepID, Name) VALUES
	('1234', 'Jessica Simmons'),
	('2903', 'Alexandra Jones'),
	('8932', 'Jerome Bird'),
	('3638', 'Sam Lincoln'),
	('2374', 'Arnold Lancaster');

-- populate Shop table

INSERT INTO Shop(ShopID, Name) VALUES
	('123', 'Books4U'),
	('122', 'Le Livre'),
	('112', 'The Bookworm'),
	('133', 'The Reading Festival'),
	('132', 'Jo''s Books');

-- populate Publisher table

INSERT INTO Publisher(PublisherID, Name) VALUES
	('10', 'Polar Bear Books'),
	('11', 'Once Upon A Time'),
	('12', 'Wish Upon A Star'),
	('13', 'Masterson Books'),
	('14', 'UEA');

-- populate Book table

INSERT INTO Book(BookID, Title, Price, CategoryID, PublisherID) VALUES
	('15', 'Henry Otter and the Pebble Stone', '12.00', '2', '10'),

	('16', 'Castle Meadows', '07.00', '1', '10'),

	('17', 'Shannon''s Day Out', '13.00', '3', '13'),

	('18', 'How to Cook: Fresher Edition', '05.45', '5', '14'),
	('19', 'How to Paint like Picasso', '04.00', '4', '11'),

	('20', 'The Adventures of Finn Huckleberry', '8.99', '2', '12'),

	('21', 'Seaside Dreams', '12.99', '1', '13'),

	('22', 'Pheobie Lorraine', '11.99', '2', '11');

-- populate ShopOrder table

INSERT INTO ShopOrder(ShopOrderID, OrderDate, ShopID, SalesRepID) VALUES
	('25', '20-01-2019', '123', '1234'),
	('26', '21-01-2019', '122', '2903'),
	('27', '22-01-2019', '112', '8932'),
	('28', '22-01-2019', '133', '3638'),
	('29', '23-01-2019', '132', '2374')
,
	('30', '24-01-3019', '123', '1234');

-- populate Orderline table

INSERT INTO Orderline(ShopOrderID, BookID, Quantity, UnitSellingPrice) VALUES
	('25', '15', '5', '10.00'),

	('25', '16', '5', '7.00'),

	('25', '17', '5', '13.00'),

	('26', '16', '3', '5.00'),

	('26', '20', '3', '8.99'),

	('26', '21', '3', '12.99'),

	('27', '17', '1', '13.00'),

	('27', '21', '1', '12.99'),

	('27', '22', '1', '11.99'),

	('28', '18', '2', '5.00'),

	('28', '21', '2', '12.99'),

	('29', '19', '4', '4.00'),

	('30', '22', '5', '11.99');