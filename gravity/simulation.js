// Get the canvas and its context
const canvas = document.getElementById('simulationCanvas');
const ctx = canvas.getContext('2d');

// Constants and variables
const FPS = 60;  // Target frames per second
let objects = []; // Array to hold all objects in the simulation
let lastTime = 0; // For calculating delta time

// Object class - for particles or other entities in your simulation
class PhysicsObject {
    constructor(x, y, mass = 1) {
        this.position = { x, y };
        this.velocity = { x: 0, y: 0 };
        this.acceleration = { x: 0, y: 0 };
        this.forces = { x: 0, y: 0 };
           this.mass = mass;
        this.radius = Math.sqrt(mass) * 10; // Size based on mass
        this.color = '#0066ff';
    }

    // Apply a force to the object
    applyForce(forceX, forceY) {
        // F = ma, so a = F/m
        this.forces.x += forceX;
        this.forces.y += forceY;
    }

    // Calculate acceleration based on forces (F = ma, so a = F/m)
    calculateAcceleration() {
        this.acceleration.x = this.forces.x / this.mass;
        this.acceleration.y = this.forces.y / this.mass;
        // Reset forces for next frame
        this.forces.x = 0;
        this.forces.y = 0;
    }

    // Update position and velocity using physics equations
    update(deltaTime) {
        // Calculate acceleration from current forces
        this.calculateAcceleration();

        // Update velocity: v = v0 + a*t
        this.velocity.x += this.acceleration.x * deltaTime;
        this.velocity.y += this.acceleration.y * deltaTime;

        // Update position: p = p0 + v*t
        this.position.x += this.velocity.x * deltaTime;
        this.position.y += this.velocity.y * deltaTime;

        // Your additional physics logic here (e.g., collisions, constraints)
        this.handleBoundaries();
    }

    // Keep objects within canvas boundaries
    handleBoundaries() {
        // Simple boundary checking (you might want more sophisticated handling)
        if (this.position.x - this.radius < 0) {
            this.position.x = this.radius;
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

    // Draw the object on the canvas
    draw() {
        ctx.beginPath();
        ctx.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.closePath();
    }
}

// Physics system - where you'll implement your natural forces
class PhysicsSystem {
    constructor() {
        // Constants for your physics calculations
        this.GRAVITY = 9.81; // m/s²
//        this.AIR_DENSITY = 1.2; // kg/m³ (approximate air density at sea level)
//        this.DRAG_COEFFICIENT = 0.47; // For a sphere (you'll implement this)
    }

    // Apply gravity to an object
    applyGravity(object, deltaTime) {
        // Implement your gravity calculation here
        // F = mg (Force = mass * gravity acceleration)
        const gravityForce = object.mass * this.GRAVITY;
        object.applyForce(0, gravityForce);
    }

    // Apply air resistance to an object
    // applyAirResistance(object, deltaTime) {
    //     // Simple temporary implementation
    //     // We'll use a basic drag force proportional to velocity
    //     const dragCoefficient = 0.1;
        
    //     // Apply drag force in opposite direction of velocity
    //     const dragForceX = -object.velocity.x * dragCoefficient;
    //     const dragForceY = -object.velocity.y * dragCoefficient;
        
    //     object.applyForce(dragForceX, dragForceY);
        
    //     /* 
    //     Later, you'll implement the proper formula:
    //     F = -0.5 * ρ * v² * A * Cd * v̂
    //     Where:
    //     ρ (rho) = air density
    //     v = velocity magnitude
    //     A = cross-sectional area
    //     Cd = drag coefficient
    //     v̂ = velocity unit vector
    //     */
    // }

    // Apply all physics forces to objects
    update(objects, deltaTime) {
        objects.forEach(object => {
            this.applyGravity(object, deltaTime);
            // this.applyAirResistance(object, deltaTime);
            // Add more forces as you develop your simulation
        });
    }
}

// Initialize the simulation
function init() {
    objects = [];
    // Create some objects for testing
    const obj1 = new PhysicsObject(400, 100, 1);
    obj1.color = '#FF0000'; // Red
    obj1.velocity.x = 50;
    
    // const obj2 = new PhysicsObject(200, 200, 2);
    // obj2.color = '#00FF00'; // Green
    // obj2.velocity.x = -30;
    
    // const obj3 = new PhysicsObject(600, 150, 3);
    // obj3.color = '#0000FF'; // Blue
    // obj3.velocity.y = 20;
    objects.push(obj1)//, obj2, obj3);

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
    physicsSystem.update(objects, deltaTime);
    
    // Update and draw objects
    objects.forEach(obj => {
        obj.update(deltaTime);
        obj.draw();
    });
}

// Initialize physics system
const physicsSystem = new PhysicsSystem();

// Start the simulation
init();
lastTime = performance.now();
requestAnimationFrame(animate);

// Optional: Add event listeners for interaction
canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    // Create a new object at the click position
    const mass = Math.random() * 3 + 0.5;
    objects.push(new PhysicsObject(x, y, mass));
});