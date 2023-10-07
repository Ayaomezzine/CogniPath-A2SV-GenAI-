var autismQuiz = {
    "Autism": [
      {
        "id": 1,
        "question": "Does your child have limited speech (non-verbal or speaks in only short phrases)?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 2,
        "question": "Does your child tend to give random answers to questions, or make random comments ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 3,
        "question": "Does your child not respond to their name ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 4,
        "question": "Does your child avoid eye contact ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 5,
        "question": "Does your child not engage in pretend play with other children ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 6,
        "question": "Does your child struggle to understand other people's feelings ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 7,
        "question": "Is your child easily upset by small changes ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 8,
        "question": "Does your child have obsessive interests ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 9,
        "question": "Does your child engage in repetitive behaviors such as hand-flapping, toe-walking, pacing, or lining up objects ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 10,
        "question": "Is your child over or under-sensitive to smells, tastes, or touch ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 11,
        "question": "Does your child struggle to socialize with other children ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 12,
        "question": "Does your child avoid physical contact ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      },
      {
        "id": 13,
        "question": "Does your child show little awareness of dangerous situations ?",
        "options": [
          { "text": "Never", "score": 0 },
          { "text": "Rarely", "score": 1 },
          { "text": "Sometimes", "score": 2 },
          { "text": "Often", "score": 3 },
          { "text": "Very Often", "score": 4 }
        ],
        "selectedOption": null
      }


      // Add more autism-related questions and answers here
    ]
  };
  
  var quizApp = function () {
    this.score = 0;
    this.currentque = 0;
  
    this.displayQuiz = function (cque) {
      this.currentque = cque;
      if (this.currentque >= autismQuiz.Autism.length) {
        // All questions have been answered
        var totalScore = this.calculateScore();
        var isAutistic = this.isAutistic(totalScore);
  
        if (isAutistic) {
          // Display a message indicating the person is autistic
          $('#result').html('<p>Your total score is ' + totalScore + '. Based on the threshold, you are considered autistic.</p>');
        } else {
          // Display a message indicating the person is not autistic
          $('#result').html('<p>Your total score is ' + totalScore + '. You are not considered autistic.</p>');
        }
  
        return;
      }
  
      $("#tque").html(autismQuiz.Autism.length);
      $("#qid").html(autismQuiz.Autism[this.currentque].id + '.');
      $("#question").html(autismQuiz.Autism[this.currentque].question);
      $("#question-options").html("");
  
      for (var i = 0; i < autismQuiz.Autism[this.currentque].options.length; i++) {
        var option = autismQuiz.Autism[this.currentque].options[i];
        $("#question-options").append(
          "<div class='form-check option-block'>" +
          "<label class='form-check-label'>" +
          "<input type='radio' class='form-check-input' name='option' data-option-index='" + i + "'>" +
          "<span id='optionval'>" + option.text + "</span>" +
          "</label>"
        );
      }
    };
  
    this.calculateScore = function () {
      var totalScore = 0;
      for (var i = 0; i < autismQuiz.Autism.length; i++) {
        var selectedOption = autismQuiz.Autism[i].selectedOption;
        if (selectedOption !== null) {
          totalScore += selectedOption.score;
        }
      }
      return totalScore;
    };
  
    this.isAutistic = function (totalScore) {
      // Define a threshold score, e.g., 20, above which the person is considered autistic
      var thresholdScore = 20;
      return totalScore >= thresholdScore;
    };
  
    this.changeQuestion = function (cque) {
      this.currentque += cque;
      this.displayQuiz(this.currentque);
    };
  };
  
  var autismQ = new quizApp();
  
  $(document).ready(function () {
    autismQ.displayQuiz(0);
  
    $('#question-options').on('change', 'input[type=radio][name=option]', function (e) {
      var questionIndex = autismQ.currentque;
      var optionIndex = $(this).data('option-index');
      autismQuiz.Autism[questionIndex].selectedOption = autismQuiz.Autism[questionIndex].options[optionIndex];
    });
  
    $('#next').click(function (e) {
      e.preventDefault();
      autismQ.changeQuestion(1);
    });
  
    $('#previous').click(function (e) {
      e.preventDefault();
      autismQ.changeQuestion(-1);
    });
  });