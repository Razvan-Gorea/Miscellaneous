class AnnalynsInfiltration {
    public static boolean canFastAttack(boolean knightIsAwake) {
        return !knightIsAwake;
    }

    public static boolean canSpy(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake) {
        return knightIsAwake || archerIsAwake || prisonerIsAwake;
    }

    public static boolean canSignalPrisoner(boolean archerIsAwake, boolean prisonerIsAwake) {
        if (archerIsAwake==false & prisonerIsAwake==true){
            return true;
        }
        return false;
    }
    
    public static boolean canFreePrisoner(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake, boolean petDogIsPresent) {
        if (petDogIsPresent==true & archerIsAwake==false){
            return true;
        }
        else if (petDogIsPresent==false & prisonerIsAwake==true & archerIsAwake==false & knightIsAwake==false){
            return true;
        }
        return false;
    }
}
