var circle = document.getElementById('cap')
var radius = circle.r.baseVal.value;
var circumference = radius * 2 * Math.PI;

circle.style.strokeDasharray = `${circumference} ${circumference}`;
circle.style.strokeDashoffset = `${circumference}`;

function setCapacity(capacity) {
  const offset = circumference - (capacity * circumference);
  circle.style.strokeDashoffset = offset;
}

var cap = circle.dataset.cap;
setCapacity(cap)