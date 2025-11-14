uniform vec3 uColor;

varying vec3 vNormal;
varying vec3 vPosition;

#include ../includes/ambientLight.glsl

#include ../includes/directionalLight.glsl

#include ../includes/pointLight.glsl

void main()
{
    vec3 viewDirection = normalize(vPosition - cameraPosition);
    vec3 color = uColor;

    // Lights
    vec3 light = vec3(0.0);
    vec3 normal = normalize(vNormal);

    // perfect red color (should dissapear with blue light)
    // light += ambientLight(vec3(1.0, 0.0, 0.0), 0.2);
    
    // dimmed white light
    // light += ambientLight(vec3(1.0), 0.2);

    // ambient light
    light += ambientLight(
        vec3(1.0), // Light color
        0.03       // Light intensity
    );

    // directional light
    light += directionalLight(
        vec3(0.1, 0.1, 1.0), // Light color
        1.0,                  // Light intensity
        normal,              // Normal
        vec3(0.0, 0.0, 3.0),  // Light position
        viewDirection,        // View direction
        20.0                 // Specular power
    );

    // point light
    light += pointLight(
        vec3(1.0, 0.1, 0.1), // Light color
        1.0,                 // Light intensity,
        normal,              // Normal
        vec3(0.0, 2.5, 0.0), // Light position
        viewDirection,       // View direction
        20.0,                 // Specular power
        vPosition,            // Position
        0.25                 // Light decay
    );

    // additional point light
    light += pointLight(
        vec3(0.1, 1.0, 0.5), // Light color
        1.0,                 // Light intensity,
        normal,              // Normal
        vec3(2.0, 2.0, 2.0), // Light position
        viewDirection,       // View direction
        20.0,                // Specular power
        vPosition,           // Position
        0.2                  // Light decay
    );

    color *= light;

    // Final color
    gl_FragColor = vec4(color, 1.0);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
}