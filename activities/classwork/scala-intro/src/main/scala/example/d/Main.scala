package example.d
import example.d.model.Visitor

object Main {
  def older(v1: Visitor,v2: Visitor): Boolean =
    v1.createAt.seconds > v2.createAt.seconds

  def a(age: Int): Visitor = Visitor.Anonymous(
    UUID.randomUUID().toString,
    Timestamp(age))

  val getUser : Int => Visitor = (age: Int) => Visitor.User (
    id = UUID.randomUUID().toString,
    email="email@example.com"
    createAt= Timestamp(age)

  )


def main(args:Array[String]): Unit = {
  val array(firstAge, secondAge) = args

  val a = getAnonymousUser(firstAge,toInt)
  val b = getUser(secondAge.toInt)

  if (older(a,b)) a.show() else b.show()
}
}
