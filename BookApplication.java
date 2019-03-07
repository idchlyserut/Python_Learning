//Passing Parameter Page 151, Q1

import java.util.*;
import java.util.Scanner;

class Book {

private String title;
private String author;
private String ISBN;
private int yearPublished;
private double price;

public Book (String title_, String author_, String ISBN_, int year_, double price_)
{

title = title_;
author = author_;
ISBN = ISBN_;
yearPublished = year_;
price = price_;
}

public void setTitle (String title_)
{
	title=title_;
}
public void setAuthor (String author_)
{
	author=author_;
}
public void setISBN (String ISBN_)
{
	ISBN=ISBN_;
}

public void setYear (int year_)
{
	yearPublished=year_;
}

public void setPrice (double price_)
{
	price=price_;
}

public String getTitle ()
{
 	return title;
 }
 public String getAuthor ()
 {
 	return author;
 }
 public String getISBN ()
 {
 	return ISBN;
 }
 public int getYear ()
 {
 	return yearPublished;
 }
 public double getPrice ()
 {
 	return price;
 }

}
public  class  BookApplication {

 public static void main(String [] args)
 {
 Book [] booklist = new Book[5];
 Book [] book = new Book[5];
 Scanner keyboard = new Scanner (System.in);
 System.out.println("Insert book details: \n");

 for (int i=0; i<booklist.length; i++)
 {

 	System.out.println("\nTitle:");
 	//String title = keyboard.nextLine();
 	//booklist[i].setTitle(title);
 	System.out.print("Author:");
 	String author = keyboard.nextLine();
 	booklist[i].setAuthor(author);
 	System.out.println("ISBN:");
 	String isbn = keyboard.nextLine();
 	booklist[i].setISBN(isbn);
 	System.out.println("Year:");
 	int year = keyboard.nextInt();
 	booklist[i].setYear(year);
 	System.out.println("Price:");
 	double price = keyboard.nextDouble();
 	booklist[i].setPrice(price);

 	book [i] = new Book (booklist[i].getTitle(),booklist[i].getAuthor(),booklist[i].getISBN(), booklist[i].getYear(),booklist[i].getPrice());
 }
}
}


/*//displayBooks(book);
calcTotalPrice(booklist.getPrice());


public static void displayBooks(Book book)
{
 	for (double val : book)
		{
		System.out.println (val + " ");
	}
}

public static Book[] calcTotalPrice(Book booklist)
{
	double temp=0.0;
	for (int i=0; i<bookilist.length; i++)
	 {
		temp[i] = temp + booklist[i];
	 }

	 return temp;
}

*/


