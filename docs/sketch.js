var h = 200;
var w = 500;
var x,y,n;
var a=10,b=3;
var data;
function preload() {
  data = loadTable("spec.csv");
}

function setup() {
  x = new Array (data.getRowCount());
  y = new Array (data.getRowCount());
  n = data.getRowCount();
  createCanvas(w, h+25);  //canvas setup
  background(0);
  frameRate(100);
  for (var i=0;i<n;i++){
    x[i]=Number(data.getRow(i).get(0));
    y[i]=Number(data.getRow(i).get(1));
  }
  var max=Math.max(...y);
  var min=Math.min(...y);
  for (i=0;i<n;i++){

    x[i]=x[i]/Math.max(...x);
    y[i]=(y[i]-min)/(max-min);
  }

}

function draw() {
  background(0);
  for (i=0;i<n-1;i+=1){
    stroke("white");
    strokeWeight(1);
    line(x[i]*w,y[i]*h+10,x[i+1]*w,y[i+1]*h+10);
    stroke("red");
    line(x[i]*w,Logistic(x[i])*h+10,x[i+1]*w,Logistic(x[i+1])*h+10);
  }
  //Train(x,y,10,0.3);
  stroke("black");
  fill("white");
  text("Error: "+Math.floor(100*Train(x,y))/100,10,15);
  text("f(x) = 1/(1+exp("+Math.floor(100*a)/100+"x + "+Math.floor(100*b)/100+"))",10,30);
  text("FPS: "+Math.floor(100*frameRate())/100,10,45);

}
function Logistic (x,der="none"){
  var f=1/(1+Math.exp(-(a*x+b)))
  if (der=="none") return f;
  else if (der=="a") return f*(1-f)*x;
  else if (der=="b") return f*(1-f);
  else if (der=="x") return f*(1-f)*a;
}
function Error (x,y,der="none"){
  var s=0
  if (der=="none") {
    s=0;
    for (i=0;i<n;i++){
      s+=(Logistic(x[i])-y[i])*(Logistic(x[i])-y[i]);
    }
    return s;
  }
  else if (der=="a" || der=="b") {
    s=0;
    for (i=0;i<n;i++){
      s+=(Logistic(x[i])-y[i])*Logistic(x[i],der);
    }
    return s;
  }
}
function Train (x,y,epoch=1,dt=0.1){
  for (i=0;i<epoch;i++){
    e=Error(x,y);
    a = a - Error (x,y,"a")*dt;
    b = b - Error (x,y,"b")*dt
  }
  return e;
}
