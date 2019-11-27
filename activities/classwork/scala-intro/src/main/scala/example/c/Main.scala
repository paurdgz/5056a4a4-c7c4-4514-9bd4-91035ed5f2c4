package example.c
import example.c.model.Box
object Main {
  val numbers: list[Int] = List(1,2,3,4,5)

  def procedure: Box[Int] =
    number.map(num=> Box(num)).foldRight(Box(0)) {
      case (elm, z) => z.concate(elm).map(_.toInt)
    }
  def main(args: Array[String]): Unit= args match{
    case valid if args.length > => procedure(args.map(_.toInt)).show()
  }
}
