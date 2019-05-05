
$(document).ready(function() {
  // Contact Form Handler
  let contactForm = $('.contact-form')
  let contactMethod = contactForm.attr('method')
  let contactFormEndpoint = contactForm.attr('action')

  function displaySubmitting(submitBtn, defaultText, doSubmit){
    if (doSubmit){
      submitBtn.addClass('disabled')
      submitBtn.html("<i class='fa fa-spin fa-spinner'></i> Sending...")
    }
    else{
      submitBtn.removeClass('disabled')
      submitBtn.html(defaultText)
    }
  }

  contactForm.submit(function(event){
    event.preventDefault();

    let contactFormSubmitBtn = contactForm.find('[type="submit"]')
    let contactFormSubmitBtnTxt = contactFormSubmitBtn.text()

    let thisForm = $(this);
    let contactFormData = thisForm.serialize();
    displaySubmitting(contactFormSubmitBtn, '', true)
    $.ajax({
      method: contactMethod,
      url: contactFormEndpoint,
      data: contactFormData,
      success: function(data){
        thisForm[0].reset();
        $.alert({
            title: 'Success',
            content: data.message,
            theme: 'modern',
        });
        setTimeout(function(){
          displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
        }, 500);
      },
      error: function(errorData){
        console.log(errorData.responseJSON)
        let jsonData = errorData.responseJSON
        let msg = ''
        $.each(jsonData, function(key, value){
          msg += key + ': ' + value[0].message + '<br/>'
        })
        $.alert({
            title: 'Oops!',
            content: msg,
            theme: 'modern',
        });
        setTimeout(function(){
          displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
        }, 500);
      },
    });

  });



  // Autosearch
  let searchForm = $('.search-form')
  let searchInput = searchForm.find("[name='q']") // input name='q'
  let typingTimer;
  let typingInterval = 500 // 1.5 seconds
  let searchBtn = searchForm.find('[type="submit"]')

  searchInput.keyup(function(event){
    // key released
    clearTimeout(typingTimer)
    typingTimer = setTimeout(performSearch, typingInterval);
  });

  searchInput.keydown(function(event){
    // key pressed
    clearTimeout(typingTimer)
  });

  function displaySearching(){
    searchBtn.addClass('disabled')
    searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
  }

  function performSearch(){
    displaySearching()
    let query = searchInput.val()
    setTimeout(function(){
      window.location.href = '/search/?q=' + query
    }, 1000);
  }


  // Cart + Add products
  let productForm = $('.form-product-ajax')
  productForm.submit(function(event){
    event.preventDefault();
    let thisForm = $(this);
    // let actionEndPoint = thisForm.attr('data-endpoint')
    let actionEndPoint = thisForm.attr('action');
    let httpMethod = thisForm.attr('method');
    let formData = thisForm.serialize();

    $.ajax({
      url: actionEndPoint,
      method: httpMethod,
      data: formData,
      success: function(data){
        // switch to submit & remove buttons asychoronusly
        let submitSpan = thisForm.find('.submit-span')
        if (data.added){
          submitSpan.html('In cart <button type="submit" class="btn btn-link">Remove</button>')
        }
        else {
          submitSpan.html('<button type="submit" class="btn btn-success">Add to cart</button>')
        }
        // update cart product count asychoronusly
        let navbarCount = $('.navbar-cart-count')
        navbarCount.text(data.cartItemCount)

        // refresh cart asychoronusly
        let currentPath = window.location.href
        if (currentPath.indexOf('cart') != -1){
          refreshCart();
        }
      },
      error: function(errorData){
        $.alert({
            title: 'Oops!',
            content: 'An error occurred',
            theme: 'modern',
        });
      },
    });

  });
  function refreshCart(){
    console.log('in current cart')
    console.log('Prevent form')
    let cartTable = $('.cart-table')
    let cartBody = cartTable.find('.cart-body')
    // cartBody.html('<h1>Changed</h1>')
    let productRows = cartBody.find('.cart-product')
    let currentUrl = window.location.href

    let refreshCartUrl = '/api/cart/'
    let refreshCartMethod = 'GET';
    let data = {};
    $.ajax({
      url: refreshCartUrl,
      method: refreshCartMethod,
      data: data,
      success: function(data){

        let hiddenCartRemoveFrom = $('.cart-item-remove-form')
        if (data.products.length > 0){
          // update cart table & display an alternative remove button asychoronusly
          productRows.html(' ')
          let i = data.products.length
          $.each(data.products, function(index, value) {
            let newCartItemRemove = hiddenCartRemoveFrom.clone()
            newCartItemRemove.css('diplay', 'block')
            // newCartItemRemove.removeClass('hidden-class')
            newCartItemRemove.find('.cart-item-product-id').val(value.id)
            cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
            i--;
          });
          cartBody.find('.cart-subtotal').text(data.subtotal)
          cartBody.find('.cart-total').text(data.total)
        }
        else{
          // reload page
          window.location.href = currentUrl
        }

      },
      error: function(errorData){
        $.alert({
            title: 'Oops!',
            content: 'An error occurred',
            theme: 'modern',
        });
      }
    });

  }

});
