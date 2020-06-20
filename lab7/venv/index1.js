$(document).ready(function () {

    $('button').on('click', function(e){
            e.preventDefault();

            var val_from, val_to, val_fun;
            val_from = $('.from').val();
            val_to = $('.to').val();
            val_from = parseFloat(val_from);
            val_to = parseFloat(val_to);
            val_fun = $('.fun').val();

            var points=[], i, j, x, k=0;
            for (i = 0; i <=val_to-val_from; i+=0.5){
                points[k]=new Array();
                for (j = 0; j < 2; j++){
                     points[k][j]=0;
                }
                k++;
            }
            k=0;
            for (i = val_to-val_from; i>= 0; i-=0.5){
                points[k][0] = val_to - i;
                x = val_to- i;
                points[k][1] = eval(val_fun);
                k++;
            }
            var dataset = [{label: val_fun ,data: points}];
            var options = {
                series: {
                    lines: { show: true },
                    }
                };
            $.plot($('.output'), dataset, options);

        });
});