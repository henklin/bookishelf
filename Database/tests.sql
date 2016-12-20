drop table shoppingCart
drop table if exists order;
drop table user
drop table book
drop table ticket

Insert into user (username, email, password, lastname, firstname, credit) values('test', 'test@test.com', 'password', 'test', 'testsson', 20000)
Insert into book (title, author, qty, price, nrSold, image, category, description) values('Harry Potter', 'JK Rowling', 15, 200, 0, 'http://prodimage.images-bn.com/pimages/9781338099133_p0_v5_s1200x630.jpg', 'fantasy', 'This is Harry Potter')
Insert into book values(2, 'The fellowship of the ring', 'JRR Tolkien', 15, 200, 0, 'https://images-na.ssl-images-amazon.com/images/I/41i-SJkyCQL._SY344_BO1,204,203,200_.jpg', 'fantasy', 'Small Ring. Big Monsters.')
Insert into book values(3, 'IT', 'Stephen King', 15, 200, 0, 'https://upload.wikimedia.org/wikipedia/en/5/5a/It_cover.jpg', 'horror', 'Scary clown')
Insert into book values(4, 'The trail', 'Franz Kafka', 15, 200, 0, 'https://images-na.ssl-images-amazon.com/images/I/51wQmxud3NL._SX331_BO1,204,203,200_.jpg', 'fiction', 'Wierd stuff')
Insert into book values(5, 'The gates of rome', 'Conn Iggulden', 15, 200, 0, 'http://www.conniggulden.com/static/uploads/default_site/book_covers/cover_emperor_the_gates_of_rome_265x407.jpg', 'history', 'Veni vidi vici')

select * from ticket

se

INSERT INTO shoppingCart (userid, bookid) VALUES(1,1)

select * from shoppingCart
delete from shoppingCart where userid=1
SELECT * FROM book ORDER BY nrSold, id desc limit 5



SELECT book.id from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=1

SELECT * from shoppingCart INNER JOIN book on book.id=shoppingCart.bookid INNER JOIN user on user.userid=shoppingCart.userid where shoppingCart.userid=1

SELECT id FROM book ORDER BY nrSold, id desc limit 5

delete from book where id=null


INSERT INTO user (firstname, lastname, username, email, password) VALUES ('test1', 'test1', 'test1', 'test@se', 'password')