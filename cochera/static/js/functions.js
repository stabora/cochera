$(document).ready(function() {
	$('.bs-tooltip').tooltip({
		'html': true
	});

	$('select[name=anio]').change(function() {
		$('form[name=grilla]').submit();
	});

	if($('#pago_form').length) {
		$('select#id_lugar').change(function() {
			if($(this).find('option:selected').text().indexOf('0:') == 0) {
				$('input#id_importe').val($('input#IMPORTE_ALQUILER_OFICINA').val());
			} else {
				$('input#id_importe').val($('input#IMPORTE_ALQUILER_COCHERA').val());
			}
		});
	}
})


$(window).load(function() {
	if($('#plano-svg').length) {
		svg = $('#plano-svg').get(0).getSVGDocument();


		$(svg).find('[id^=lugar]')
		.attr('cursor', 'pointer')
		.click(function()
		{
			select_lugar(get_lugar($(this).attr('id')));
		});

		$('tr[id^=lugar]').click(function() {
			select_lugar(get_lugar($(this).attr('id')));
		});

		$('tr[id^=lugar][class*=desocupado]').each(function() {
			lugar = get_lugar($(this).attr('id'));
			$(svg).find('rect[id=' + lugar + ']').css('stroke-dasharray', '2');
			$(svg).find('g[id=' + lugar + '_texto]').find('path').css('fill', '#CACACA').css('stroke', '#CACACA');
			$(svg).find('g[id=' + lugar + '_texto]').find('text').css('fill', '#000000');
		})

		$('tr[id^=lugar][class*=alerta-atraso]').each(function() {
			lugar = get_lugar($(this).attr('id'));
			$(svg).find('g[id=' + get_lugar($(this).attr('id')) + '_texto]').find('path').css('fill', '#ff0000').css('stroke', '#ff0000');
		})
	}
});


function get_lugar(lugar) {
	if(lugar.indexOf('_') > -1) {
		lugar = lugar.substr(0, lugar.indexOf('_'));
	}

	return lugar;
}

function select_lugar_tabla(lugar) {
	$('tr[id^=lugar]').removeClass('success');
	$('tr#' + lugar + '_row').toggleClass('success');
}

function select_lugar_plano(lugar) {
	$(svg).find('rect[id^=lugar]').css('fill', '#ffffff');
	$(svg).find('rect[id=' + lugar + ']').css('fill', '#dff0d8');
}

function select_lugar(lugar) {
	select_lugar_tabla(lugar);
	select_lugar_plano(lugar);
}
