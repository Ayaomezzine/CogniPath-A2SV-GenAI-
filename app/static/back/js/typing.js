        // JavaScript to dynamically set the text and width
        const paragraph = "Generated image:";

        // Select the element
        const dynamicTextElement = document.getElementById("dynamic-text");

        // Set the text content
        dynamicTextElement.textContent = paragraph;

        // Calculate and set the width based on the content length
        dynamicTextElement.style.width = `${paragraph.length}ch`;