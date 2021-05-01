
public class Student extends User{
	private String studentNumber;
	public Student(int id,String firstName,String lastName,String email,String password, String studentNumber) {
		super(id,firstName,lastName,email,password);
		this.studentNumber=studentNumber;
}

}
