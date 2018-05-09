const int doPin = 8;
const int rePin = 9;
const int miPin = 10;
const int faPin = 4;
const int soPin = 5;
const int laPin = 6;
const int tiPin = 7;
const int b1Pin = 2;
const int b2Pin = 3;
const int b3Pin = 11;
const int b4Pin = 12;
const int b5Pin = 13;

int ready_for_next_note = true;

String notes[12] = { "DO", "B1", "RE", "B2", "MI", "FA", "B3", "SO", "B4", "LA", "B5", "TI"};

void setup() {
  Serial.begin(115200);
}

void play_note(int note, bool ready_for_next_note){
  if (digitalRead(note) == HIGH && ready_for_next_note){
    ready_for_next_note = false;
    Serial.println(notes[note-2]);
  }
}

void check_ready(){
  ready_for_next_note = true;
  for(int i = 2; i<= 13; i++){
    if (digitalRead(i) == HIGH){
      ready_for_next_note = false;    
    }
  }
}

void loop() {
  for(int i = 2; i<= 13; i++){
    play_note(i, ready_for_next_note);
  }
  check_ready();
  delay(30);
}
