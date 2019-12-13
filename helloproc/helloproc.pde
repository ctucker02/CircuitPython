int a = 150;
int b = 150;
// circles starting position 
int c = 1;
int d = 5;
// circle changes vertically 5x fast; makes it bounce around on the screen
void setup ()
{
  size (300, 300);
  // makes the screen 300 x 300
  background (255, 0, 0);
  // colors it red
}
void draw ()
// just like "void loop" in arduino
{
  background (255, 0 , 0);
  // redraw the background each time, to prevent the circle from leaving a line
  ellipse (a, b, 150, 150);
  // make a 150 x 150 circle
  fill (0, 0, 255);
  // color it blue
  if (a >= 225 || a <= 75)
  // when the circle hits the end of the screen
    {
      c = -c;
      //switch directions
    }
   if (b >= 225 || b <= 75)
   {
     d = -d;
   }
   a = a + c;
   b = b + d;
   // increase/decrease a and b by the designated amounts
   println ("Hello world.");
}
