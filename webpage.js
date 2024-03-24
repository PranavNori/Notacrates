const startButton = document.getElementById("startRecording");
      const outputDiv = document.getElementById("output");

      if (
        "SpeechRecognition" in window ||
        "webkitSpeechRecognition" in window ||
        "mozSpeechRecognition" in window ||
        "msSpeechRecognition" in window
      ) {
        const recognition = new (window.SpeechRecognition ||
          window.webkitSpeechRecognition ||
          window.mozSpeechRecognition ||
          window.msSpeechRecognition)();
        recognition.lang = "en-US";

        recognition.onstart = () => {
          startButton.textContent = "Listening...";
        };

        recognition.onresult = (event) => {
          const transcript = event.results[0][0].transcript;
          outputDiv.textContent = transcript;
        };

        recognition.onend = () => {
          startButton.textContent = "Start Voice Input";
        };

        startButton.addEventListener("click", () => {
          recognition.start();
        });
      } else {
        outputDiv.textContent =
          "Speech Recognition API not supported in this browser.";
      }