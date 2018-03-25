/*jshint expr: true */

!(function() {
    'use strict';

    var element = document.getElementsByClassName('reputation-widget')[0];
    if (element) {
        //console.log(element)
        var tk = element.getAttribute('data-tk'),
            lk = element.getAttribute('data-lk'),
            lc = element.getAttribute('data-lc'),
            widgetId = element.getAttribute('data-widget-id'),
            env = element.getAttribute('env'),
            protocol = /^http:/.test(document.location) ? 'http' : 'https',
            iframe,
            widget
            console.log(widget)
            console.log(lk)
            console.log(lc);
    

        // Create iframe
        iframe = document.createElement('iframe');
        iframe.id = 'reputation-widget-0'; // HTML iframe Element
        iframe.style.border = '1px solid #ccc';

        // Determine iframe src
        if (env && env === 'local') {
            iframe.src = 'http://localhost:3334/';
        } else {
            iframe.src = protocol + '://' + (env ? env + '-' : '') + 'widgets.reputation.com/';
        }
        iframe.src += 'widgets/' + widgetId + '/run?tk=' + tk;

        if (lc) {
            iframe.src += '&lc=' + lc;
            console.log(lc)
        } else if (lk) {
            console.log(lk)
            iframe.src += '&lk=' + lk;
        }

        // Apply widget parameters 
        
        //A reference to the window object that sent the message; you can use this to establish 
        //two-way communication between two windows with different origins.
        window.addEventListener('message', function(event) {
        if('message') throw err;

            widget = event.data; // using the message with current date and time.
            console.log(widget)

            if (widget.id === widgetId) {
                console.log(widget.id)
                console.log(widgetId)
                console.log(widget.name)
                iframe.title = widget.name;

                if (widget.parameters) {
                    if (widget.parameters.width && widget.parameters.widthUnits) {
                        iframe.style.width = widget.parameters.width + widget.parameters.widthUnits;
                    }

                    if (widget.parameters.height) {
                        console.log(widget.parameters.height)
                        iframe.style.height = widget.parameters.height + 'px';
                    }
                }
            }
        });

        // Replace element
        element.parentNode.replaceChild(iframe, element);
    }

}());