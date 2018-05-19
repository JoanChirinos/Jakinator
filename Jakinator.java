/*
       __                     ________    _      _
      / /___  ____ _____     / ____/ /_  (_)____(_)___  ____  _____
 __  / / __ \/ __ `/ __ \   / /   / __ \/ / ___/ / __ \/ __ \/ ___/
/ /_/ / /_/ / /_/ / / / /  / /___/ / / / / /  / / / / / /_/ (__  )
\____/\____/\__,_/_/ /_/   \____/_/ /_/_/_/  /_/_/ /_/\____/____/

~Joan Chirinos, May 18, 2018
*/

/*
Like Akinator, but Joan's version
*/

import java.util.HashMap;
import jutils.*;
import java.awt.Desktop;
import java.net.URI;

public class Jakinator {

  private HashMap<String, String> _map;

  public Jakinator() {
    _map = new HashMap<String, String>();
    String[] fileContents = FileRW.read("qa.txt").split("\n");
    for (String s : fileContents) {
      String[] kvp = s.split(",");
      _map.put(kvp[0], kvp[1]);
    }
  }

  public void run() {
    String currKey = "0";
    while (true) {

      //if the choice we're on doesn't exist, question everything
      if (!_map.containsKey(currKey)) {
        System.out.println("What");
        throw new IndexOutOfBoundsException("wyd");
      }

      //if current index is a question, print it and ask for answer
      else if (_map.get(currKey).charAt(0) == 'Q') {
        while (true) {

          System.out.println(_map.get(currKey).substring(1));
          System.out.println("\t1. Yes\n\t2. No");
          String answer = Keyboard.readString();

          //if the answer is yes, go to "yes" subtree. if answer is no, go to "no" subtree
          if (answer.equals("1")) {
            currKey += "1";
            break;
          }
          else if (answer.equals("2")) {
            currKey += "0";
            break;
          }

          //if the answer is invalid, try again
          else System.out.println("Invalid answer...\n\n");

        }
      }

      //if current index is question, print and ask if correct
      else if (_map.get(currKey).charAt(0) == 'A') {

        while (true) {

          System.out.println("Is this who you were thinking of?\n" + _map.get(currKey).substring(1));
          System.out.println("\t1. Yes\n\t2. No");
          String answer = Keyboard.readString();

          //if the answer is yes, we're done. if the answer is no, continue
          if (answer.equals("1")) {
            System.out.println("Voila!");
            return;
          }
          else if (answer.equals("2")) {
            break;
          }

          //if the answer is invalid, try again
          else System.out.println("Invalid answer...\n\n");

        }

        //if we're here, guess was incorrect

        //store correct person
        System.out.print("You were thinking of: ");
        String correctPerson = "A" + Keyboard.readString();

        System.out.println("\n");

        //store new question
        System.out.println("A yes or no question to differentiate " + _map.get(currKey).substring(1) + " from " + correctPerson + " is:");
        String newQuestion = "Q" + Keyboard.readString();

        while (true) {

          System.out.println("If the answer to \"" + newQuestion + "\" is yes, then the person is\n\t1. " + correctPerson + "\n\t2. " + _map.get(currKey).substring(1));
          String whichIsRight = Keyboard.readString();

          if (!whichIsRight.equals("1") && !whichIsRight.equals("2")) System.out.println("Invalid answer...\n\n");
          else break;

        }

        System.out.println("Thanks very mucho!");
        String url = "http://homer.stuy.edu/~jchirinos/Jakinator/go.py?";
        //add newCharacter
        url += "newCharacter=" + newCharacter.replace(" ", "+");
        //add newQuestion
        url += "&question=" + 
        if (Desktop.isDesktopSupported()) {
          try {
            Desktop.getDesktop().browse(new URI(newCharacter.replace(" ", "+") + "&question=" + newQuestion.));
          }
          catch (Exception e) {
            System.out.println("whoa");
          }
        }

      }

    }
  }

  public static void main(String[] args) {
    Jakinator j = new Jakinator();
    j.run();
  }

}//end class