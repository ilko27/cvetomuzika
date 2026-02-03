int normIntensity = 255;
int lastIntensity = 0;

const int RED = 3;
const int GREEN = 5;
const int BLUE = 6;
const int PINS[] = { RED, GREEN, BLUE, 10 };

const byte START = 0x01;

int i = 0;

int rgb[] = { 0, 0, 0, 0 };
int last_rgb[] = { 0, 0, 0, 0 };

void setup() {
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {
  if (Serial.available() >= 6) {
    if (Serial.read() == START) {
      if (Serial.read() == 3) {
        rgb[0] = Serial.read();
        rgb[1] = Serial.read();
        rgb[2] = Serial.read();
        if(Serial.read() != (rgb[0] ^ rgb[1] ^ rgb[2])) return;
      }
    }
  }
  for (i = 0; i < 3; i++) {
    if (rgb[i] < 0) {
      rgb[i] = last_rgb[i];
    }
    if (rgb[i] > 255) {
      rgb[i] = 255;
    }

    analogWrite(PINS[i], rgb[i]);
    last_rgb[i] = rgb[i];
  }
}
