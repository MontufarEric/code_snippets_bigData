//Scala word count
import java.io.{BufferedWriter, File, FileWriter}

import scala.io.Source
import scala.collection.immutable.ListMap

object StaticReference {
  def main(args: Array[String]): Unit = {
    //Create a list of sentences from a file
    val lines = Source.fromFile("/home/fieldengineer/Documents/Shakespeare.txt").getLines.toList
    // Create a list of words splitted by space, comma, dot, hyphen, etc
    val words = lines.flatMap(line => line.split(" |/.|/, |/-|/'|/!|/;|/,|/. |/:"))
    //Map each word with a one
    val keyData = words.map(word => (word, 1))
    //Group each word
    val groupedData = keyData.groupBy(ite => ite._1)
    //Get the sum of values
    val result = groupedData.mapValues(list => {
      list.map(ite => ite._2).sum
    })

    // sort the map by word frequency
    val sortedResult = ListMap(result.toSeq.sortWith(_._2 > _._2):_*)
    println(sortedResult)

    // create a file to add the word frequencies
    val file = new File("/home/fieldengineer/Documents/wc_.txt")
    val bw = new BufferedWriter(new FileWriter(file))

    // add a header to the file and write each word, freq pair in the file
    bw.write("Word, frequency \n")
    for (line <- sortedResult){
      bw.write(s"${line._1}, ${line._2} \n")
    }
    // close the file
    bw.close()
    sortedResult.foreach(println)
  }
}

