import java.util.ArrayList;

public class PlaneSeats {
	
	public ArrayList<String> seats = new ArrayList<String>();
	
	public ArrayList<String> getSeats() {
	    return seats;
	}
	
	public void fillSeat(String value) {
		getSeats().add(value);
	}
	
	//Only when is First Class
	public boolean areSeatsFull() {
		return getSeats().size() == 5;
	}
	
	public int nextSeat() {
		return getSeats().size();
	}

}
