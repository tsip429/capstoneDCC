int i;
void setup() {
  size(1000,1000);
  background(200);
  noFill();
  i = 0;
}

void draw(){
  int snowflakeSize = height/10;
  for (int snowflake = snowflakeSize; snowflake < width; snowflake+=snowflakeSize){
    for (int snowflake2 = snowflakeSize; snowflake2 < height;  snowflake2+=snowflakeSize){ 
      fill(255);
      pushMatrix();
      translate(snowflake, snowflake2);
      rotate(radians(i));
      rect(0, 0, 1000/10, 1000/10);
      popMatrix();
    }
  }
  i++;
  int snowSize = 300;
  fill(50, 100, 240);
  ellipse(500, 600, snowSize, snowSize);
  ellipse(500, 400, snowSize-100, snowSize-100);
  ellipse(500, 250, snowSize-150, snowSize-150);
  fill(230, 100, 50);
  triangle(450, 230, 450, 270, 350, 250);
  /*for (int snowman = 600; snowman < height; snowman-=snowSize){
    if (snowSize > 0){
    ellipse(snowman, snowman + 50, snowSize, snowSize);
    snowSize-=100;
    }
  }*/
}