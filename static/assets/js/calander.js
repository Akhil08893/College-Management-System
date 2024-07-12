document.addEventListener('DOMContentLoaded', function() {
	var calendarEl = document.getElementById('calendar');
  
	var calendar = new FullCalendar.Calendar(calendarEl, {
	  initialView: 'dayGridMonth', // Adjust the view as needed (dayGridMonth, timeGridWeek, etc.)
	  events: [ // Replace with your event data (date, title, etc.)
		{ title: 'Event 1', start: '2024-07-15' },
		{ title: 'Event 2', start: '2024-07-20' }
	  ]
	});
  
	calendar.render();
  });
  