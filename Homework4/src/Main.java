
public class Main {

	public static void main(String[] args) {
		Student student1 = new Student(1,"ahmet","dogan","asddswwwqqdads@dsadsddssd","atl�123456","12345");
		StudentManager studentManager=new StudentManager();
		Instructor �nstructor1=new Instructor(2, "hasan", "altay", "ddsasdasdsa@hashashsahsah", "123456789");
		InstructorManager �nstructorManager=new InstructorManager();
		studentManager.add(student1);
		�nstructorManager.add(�nstructor1);
	}

}
