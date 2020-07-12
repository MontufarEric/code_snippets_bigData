import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.io.File;  // Import the File class 
import java.io.FileInputStream;
import java.util.Scanner; // Import the Scanner class to read text files

public class Word_Counter {

	public static void main(String[] args)
	{
	  try
		{
			FileInputStream myObj = new FileInputStream("/home/fieldengineer/Documents/Shakespeare.txt");
			Scanner myReader = new Scanner(myObj);
			ArrayList<Integer> Count = new ArrayList<Integer>();
	        ArrayList<String> word = new ArrayList<String>();
			while (myReader.hasNext()) 
			{
		        String nextWord = myReader.next();
		        if (word.contains(nextWord))
		        {
		        	int index = word.indexOf(nextWord);
		        	Count.set(index, Count.get(index)+1);
		        }
		        else {
		        	word.add(nextWord);
		        	Count.add(1);
		        }
		       
			}
			
			for (int i =0; i <word.size(); i++)
			{
				System.out.print(word.get(i) + ":" + Count.get(i) + " " );
			}
			myReader.close();
			
		}
		catch (FileNotFoundException e)
		{
			System.out.print("There was an error");
		}
	}
}
