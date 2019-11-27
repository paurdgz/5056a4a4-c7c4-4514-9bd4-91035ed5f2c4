package example.c.model

case class Box[A](value: A) {

  def show(): Unit =print(value)
  def map[B](f: A => B): Box[B] = Box(fn(value))

  def flatMap(f: A => Box[A]): Box[A] = fn(value)
  def concat (other: Box[A]): Box[String]=
    Box(value.toString + other.)

}
