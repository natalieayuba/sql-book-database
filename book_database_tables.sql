-- an SQL program to create the tables in the database 

CREATE SCHEMA BookWholesalerDatabase;

SET SEARCH_PATH TO BookWholesalerDatabase, PUBLIC;

CREATE TABLE Category (
	CategoryID		INTEGER			NOT NULL,
	Name			VARCHAR(50)		NOT NULL,		
	CategoryType 		VARCHAR(20)		NOT NULL	CHECK(CategoryType IN ('Fiction','Non-fiction')),
	CONSTRAINT PK_Category PRIMARY KEY(CategoryID)
);

CREATE TABLE SalesRep (
	SalesRepID		INTEGER			NOT NULL,
	Name			VARCHAR(50)		NOT NULL,
	CONSTRAINT PK_SalesRep PRIMARY KEY(SalesRepID)
);

CREATE TABLE Shop (
	ShopID			INTEGER			NOT NULL,
	Name			VARCHAR(50)		NOT NULL,
	CONSTRAINT PK_Shop PRIMARY KEY(ShopID)
);

CREATE TABLE Publisher (
	PublisherID		INTEGER			NOT NULL,
	Name			VARCHAR(50)		NOT NULL,
	CONSTRAINT PK_Publisher PRIMARY KEY(PublisherID)
);

CREATE TABLE Book (
	BookID			INTEGER			NOT NULL,
	Title			VARCHAR(50)		NOT NULL,
	Price			DECIMAL(10,2)		NOT NULL	CHECK(Price>0),
	CategoryID		INTEGER			NOT NULL,
	PublisherID		INTEGER			NOT NULL,
	CONSTRAINT PK_Book PRIMARY KEY(BookID),
	CONSTRAINT FK1_Book FOREIGN KEY(CategoryID) REFERENCES Category,
	CONSTRAINT FK2_Book FOREIGN KEY(PublisherID) REFERENCES Publisher
);

CREATE TABLE ShopOrder (
	ShopOrderID		INTEGER			NOT NULL,
	OrderDate		DATE			NOT NULL,
	ShopID			INTEGER			NOT NULL,
	SalesRepID		INTEGER			NOT NULL,
	CONSTRAINT PK_ShopOrder PRIMARY KEY (ShopOrderID),
	CONSTRAINT FK1_ShopOrder FOREIGN KEY(ShopID) REFERENCES Shop	ON DELETE CASCADE	ON UPDATE CASCADE,
	CONSTRAINT FK2_ShopOrder FOREIGN KEY(SalesRepID) REFERENCES SalesRep
);

CREATE TABLE Orderline (
	ShopOrderID		INTEGER			NOT NULL,
	BookID			INTEGER			NOT NULL,
	Quantity		INTEGER			NOT NULL	CHECK(Quantity>0),
	UnitSellingPrice	DECIMAL (10,2)		NOT NULL	CHECK(UnitSellingPrice>0),
	CONSTRAINT PK_Orderline PRIMARY KEY (ShopOrderID, BookID),
	CONSTRAINT FK1_Orderline FOREIGN KEY(ShopOrderID) REFERENCES ShopOrder,
	CONSTRAINT FK2_Orderline FOREIGN KEY(BookID) REFERENCES Book
);			
