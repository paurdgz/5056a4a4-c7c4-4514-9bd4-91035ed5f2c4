package example

object Hello {
  val default = "World"

  //Greeting function
  def greeting (name: String = default): String  = {
   s"Hello, $name!"
 }

  //Main method
  // run with : sbt "runMain example.Hello World"
  def main(args: Array[String]): Unit = {
    val name = args.headOption.getOrElse(default)
    println(greeting(name))
  }

}