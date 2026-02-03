int normIntensity = 255;
int lastIntensity = 0;

const int RED = 3;
const int GREEN = 5;
const int BLUE = 6;
const int PINS[] = { RED, GREEN, BLUE };

int i = 0;

int last_rgb[3] = { 0, 0, 0 };

void setup() {
  Serial.begin(9600);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
}

void loop() {
  char haha[4];
  Serial.readBytes(haha, 4);

  Serial.println(haha);
  normIntensity = '\n';
  // Serial.readBytes()
  if (normIntensity == '\n') {
    i = 0;
    return;
  }
  if (i > 2) {
    i = 0;
    return;
  }

  if (normIntensity < 0) {
    normIntensity = last_rgb[i];
  }
  if (normIntensity > 255) {
    normIntensity = 255;
  }

  Serial.print("i is: ");
  Serial.println(i);
  analogWrite(PINS[i], normIntensity);
  last_rgb[i] = normIntensity;
  i++;
  // lastIntensity = normIntensity;
}
