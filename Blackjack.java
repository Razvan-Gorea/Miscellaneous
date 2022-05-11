public class Blackjack {
    //- Stand (S)
    //- Hit (H)
    //- Split (P)
    //- Automatically win (W)
    
    // we will assume that aces can only take the value of 11 for simplicity.
    //card	value	card	value
    //ace	 11	   eight	 8
    //two	 2	   nine	     9
    //three	 3	   ten	     10
    //four	 4	   jack	     10
    //five	 5	   queen	 10
    //six	 6	   king	     10
    //seven	 7	   other	 0
        public int parseCard(String card) {
            if (card == "ace"){
                return 11;
            }else if (card == "jack" || card == "queen" || card == "king" || card == "ten" ){
                return 10;
            }else if (card == "nine"){
                return 9;
            }else if (card == "eight"){
                return 8;
            }else if (card == "seven"){
                return 7;
            }else if (card == "six"){
                return 6;
            }else if (card == "five"){
                return 5;
            }else if (card == "four"){
                return 4;
            }else if (card == "three"){
                return 3;
            }else if (card == "two"){
                return 2;
            }else {
                return 0;
            }
        }
    
        public boolean isBlackjack(String card1, String card2) {
            int cardsTotal = parseCard(card1) + parseCard(card2);
            if (cardsTotal == 21){ 
                return true;
            }else {
                return false;
            } 
        }
    
        public String largeHand(boolean isBlackjack, int dealerScore) {
            if (isBlackjack == false){
                return "P";
            }
            else if (isBlackjack == true && dealerScore < 10){
                return "W";
            }else if (isBlackjack == true && dealerScore > 10){
                return "S";
            }else{
                return "S";
            }
        }
    
        public String smallHand(int handScore, int dealerScore) {
            if (handScore >= 17){
                return "S";
            }else if (handScore <= 11){
                return "H";
            }else if (handScore >= 12 && handScore <= 16 && dealerScore <= 6){
                return "S";
            }else if (handScore >= 12 && handScore <= 16 && dealerScore >= 7){
                return "H";
            }else{
                return "S";
            }
        }
    
        public String firstTurn(String card1, String card2, String dealerCard) {
            int handScore = parseCard(card1) + parseCard(card2);
            int dealerScore = parseCard(dealerCard);
            if (20 < handScore) {
                return largeHand(isBlackjack(card1, card2), dealerScore);
            } else {
                return smallHand(handScore, dealerScore);
            }
        }
    }