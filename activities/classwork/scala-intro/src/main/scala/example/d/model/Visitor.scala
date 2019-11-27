package example.d.model

import java.sql.Timestamp

trait Visitor {
  def id: String
  def CreateAt: Timestamp

  def getAgeinSeconds: Int = createAt.seconds
  def show(): Unit = this match {
    case Visitor.Anonymous(id, createAt) =>
      printIn(s"Anonymous super with id $id")
    case Visitor.User(_, email, _) =>
      printIn(s"User with email  $email")
  }

  def getEmail: Option[String]


}

object Visitor {
  final case class Anonymous(id: String, createAt: Timestamp) extends Visitor
  final case class User(id: String, email: String, createAt: Timestamp) extends Visitor
}