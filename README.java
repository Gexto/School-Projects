# School-Projectsimport java.util.Scanner;
import java.util.Arrays;

public class Reservation {
	
	public static void main(String[] args) {
		PlaneSeats firstClass = new PlaneSeats();
		PlaneSeats economy = new PlaneSeats();
		
		Scanner object = new Scanner(System.in);
		
		do {
			System.out.println("Please select of the following options below:");
			System.out.println("Press 1 for First Class");
			System.out.println("Press 2 for Economy");
			int input = object.nextInt();
			int nextSeat = 0;
			
			
			if (input == 1) {
				if(firstClass.areSeatsFull()) {
					//if there are no seats available in first class; then
					//, check to see if there are seats in the economy, 
					//and print 
					System.out.println("Unfortunately, there are no more seats in first class.");
					System.out.println("Would you like to fly economy Would you like to "
							+ "reserve another seat?");
					System.out.println("Press 1- Yes"); 
					System.out.println("Press 2- no");
					input = object.nextInt();
					
					if(input == 1) {
						nextSeat = economy.nextSeat();
						economy.fillSeat(nextSeat+"");
						System.out.println("Your seat in economy is number " + (nextSeat+1) + 
								" Thanks for flying with us.");
					}
					else {
						System.out.println("Have a nice day!");
					}
					

					
				}else {
					nextSeat = firstClass.nextSeat();
					firstClass.fillSeat(nextSeat+"");
					System.out.println("Your seat in first class is number " + (nextSeat+1) + 
							" Thanks for flying with us.");
				}
				
			}else if (input == 2) {
				nextSeat = economy.nextSeat();
				economy.fillSeat(nextSeat+"");
				System.out.println("Your seat in economy is number " + (nextSeat+1) + 
						" Thanks for flying with us.");
				
			}else {
				//print wrong choice
				System.out.println("User Error: The choice that you"
						+ " entered is not valid. Please try again. ");
			}
			
			
		}while(true);
		
		
	}
	

	
}
