// Get the canvas and its context
const canvas = document.getElementById('simulationCanvas');
const ctx = canvas.getContext('2d');

// Constants and variables
const FPS = 60;  // Target frames per second
let objects = []; // Array to hold all objects in the simulation
let lastTime = 0; // For calculating delta time



class geometricRectangle
{
    constructor(x , y, f, g, a = 0, b = 0, )
    {

        this.position = {x, y};
        this.height = Math.random() * 100 ;
        this.width =  Math.random() * 100 ;
        this.velocity = {a:0, b:0}; // speed in each component, a for x-axis and b for y-axis
        this.acceleration = {f:0, g:0} //acceleration in each component, f for x-axis and g for y-axis
    }

    applyForces(accelerationx, accelerationy){
        this.acceleration.f = accelerationx
        this.acceleration.g = accelerationy
    }

    update(deltaTime){
        this.velocity.a += deltaTime * this.acceleration.f 
        this.velocity.b += deltaTime * this.acceleration.g

        this.position.x += deltaTime * this.velocity.a
        this.position.y += deltaTime * this.velocity.b

        this.handleBoundaries();

    }

    handleBoundaries() {
    // Simple boundary checking (you might want more sophisticated handling)

        if (this.position.x  < 0) {
            this.position.x = 0;
            this.velocity.x *= -1; // Bounce without energy loss
        }
        if (this.position.x + this.radius > canvas.width) {
            this.position.x = canvas.width - this.radius;
            this.velocity.x *= -0.8; // Bounce without energy loss
        }
        if (this.position.y - this.radius < 0) {
            this.position.y = this.radius;
            this.velocity.y *= -0.8; // Bounce without energy loss
        }
        if (this.position.y + this.radius > canvas.height) {
            this.position.y = canvas.height - this.radius;
            this.velocity.y *= -0.8; // Bounce withouit energy loss
        }
    }


    draw()
    {
        ctx.beginPath();
        ctx.rect(this.position.x, this.position.y, this.height, this.width);
        ctx.fillStyle = "#0066ff";
        ctx.fill();
        ctx.closePath();
    }
}


class PhysicsSystem {
    constructor() {
        this.GRAVITYCONSTANT = 9.81; //          meter / second * second
    }

    applyGravity(object) {
        const gravityAcceleration =  this.GRAVITYCONSTANT;
        object.applyForces(0, gravityAcceleration);
    }

    update(objects, deltaTime) {
        objects.forEach(object => {
            this.applyGravity(object, deltaTime);
        });
    }
}


// Initialize the simulation
function init() {
    objects = [];

    const obj1 = new geometricRectangle(50, 50);
    const obj2 = new geometricRectangle(350, 500);

    objects.push(obj1, obj2);

}

// Main animation loop
function animate(currentTime) {
    requestAnimationFrame(animate);
    
    // Calculate delta time in seconds (for consistent physics regardless of frame rate)
    const deltaTime = (currentTime - lastTime) / 1000;
    lastTime = currentTime;
    
    // Skip if delta time is too large (e.g., when tab was inactive)
   // if (deltaTime > 0.1) return;
    
    // Clear canvas
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Update physics
    // physicsSystem.update(objects, deltaTime);
    
    // Update and draw objects
    objects.forEach(obj => {
     //   obj.update(deltaTime);
        obj.draw();
    });
}

// Initialize physics system
// const physicsSystem = new PhysicsSystem();

// Start the simulation
init();
lastTime = performance.now();
requestAnimationFrame(animate);

// Optional: Add event listeners for interaction
