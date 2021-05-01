
public class Main {

	public static void main(String[] args) {
		Student student1 = new Student(1,"ahmet","dogan","asddswwwqqdads@dsadsddssd","atlı123456","12345");
		StudentManager studentManager=new StudentManager();
		Instructor ınstructor1=new Instructor(2, "hasan", "altay", "ddsasdasdsa@hashashsahsah", "123456789");
		InstructorManager ınstructorManager=new InstructorManager();
		studentManager.add(student1);
		ınstructorManager.add(ınstructor1);
	}

}
