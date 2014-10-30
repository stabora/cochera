	$(document).ready(function() {
		$('.bs-tooltip').tooltip({ html: true });

		$('select[name=anio]').change(function() {
			$('form[name=grilla]').submit();
		});
	})