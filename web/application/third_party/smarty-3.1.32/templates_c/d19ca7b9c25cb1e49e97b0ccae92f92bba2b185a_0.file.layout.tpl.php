<?php
/* Smarty version 3.1.33, created on 2018-12-22 03:53:21
  from '/var/www/html/application/views/layout.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5c1d8b015614d0_01595657',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'd19ca7b9c25cb1e49e97b0ccae92f92bba2b185a' => 
    array (
      0 => '/var/www/html/application/views/layout.tpl',
      1 => 1545438627,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5c1d8b015614d0_01595657 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, false);
?>
<!DOCTYPE html>
<html lang="tr" prefix="og: http://ogp.me/ns#">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_10268026555c1d8b0155f4c7_69409046', 'meta');
?>

  <title>Front End Development</title>
  <link rel="icon" href="/assets/images/favicon.png">

  <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_17983007455c1d8b0155f944_95090152', 'top_js');
?>



  <!-- Google Tag Manager -->
  <?php echo '<script'; ?>
>(function (w, d, s, l, i) {
      w[l] = w[l] || [];
      w[l].push({
        'gtm.start':
          new Date().getTime(), event: 'gtm.js'
      });
      var f = d.getElementsByTagName(s)[0],
        j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
      j.async = true;
      j.src =
        'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
      f.parentNode.insertBefore(j, f);
    })(window, document, 'script', 'dataLayer', 'GTM-WVNS65V');<?php echo '</script'; ?>
>
  <!-- End Google Tag Manager -->

  <link rel="stylesheet" href="/assets/css/font-awesome.min.css">
  <link rel="stylesheet" href="/assets/main.css">
  <link rel="stylesheet" href="/assets/css/footer.css">
  <link rel="stylesheet" href="/assets/css/core.css">
  <link rel="stylesheet" href="/assets/css/bootstrap-select.css">
  <link rel="stylesheet" href="/assets/css/gp/gpmodal.css">
  <link rel="stylesheet" href="/assets/css/gp/gp-popup.css">

  <style type="text/css">iframe.goog-te-banner-frame {
      display: none !important;
    }</style>
  <style type="text/css">body {
      position: static !important;
      top: 0px !important;
    }</style>
  <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_8656370275c1d8b0155fd94_10834086', 'css');
?>


  <!--<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.0/css/all.css" integrity="sha384-lKuwvrZot6UHsBSfcMvOkWwlCMgc0TaWr+30HWe3a4ltaBwTZhyTEggF5tJv8tbt" crossorigin="anonymous">-->
  <!--<link href="https://fonts.googleapis.com/css?family=Lato:300,300i,400,700,900|Merriweather:300,400,700,900|Montserrat:300,400,500,600,700,800,900|Playfair+Display:400,400i,700,700i,900,900i|Raleway:300,300i,400,500,600,700,800,900|Roboto:300,300i,400,500,700,900" rel="stylesheet">-->

</head>

<body>
<!-- Google Tag Manager (noscript) -->
<noscript>
  <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WVNS65V"
          height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>
<!-- End Google Tag Manager (noscript) -->
<!-- NAVIGATION START-->


<input type="hidden" id="currency" value="TRY">
<input type="hidden" id="language" value="turkish">
<input type="hidden" id="language_abbr" value="tr">
<input type="hidden" id="active_tab" value="anasayfa">
<input type="hidden" id="logEnabled" value="true">
<input type="hidden" id="errorEnabled" value="true">
<nav id="navbar" class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark " style="background-color: #000 !important;z-index: 10000">
  <div id="navbarContainer" class="container ">


    <a href="https://dev-front.goodparents.com/" class="navbar-brand"><img class="header-goodparents-logo" src="/assets/images/logo.png" alt="Good Parents"></a>


    <button id="navbar-toggler-button" class="navbar-toggler" data-toggle="collapse" data-target="#navbarMenu">
      <span class="navbar-toggler-icon"></span>
    </button>


    <div class="collapse navbar-collapse" id="">

      <ul class="navbar-nav ml-auto mr-xl-5">
        <li class="nav-item">
          <a id="anasayfa_tab" href="https://www.goodparents.com/" class="nav-link gp_lang_t_home ">Anasayfa</a>
        </li>
        <li class="nav-item">
          <a id="hakkimizda_tab" href="https://www.goodparents.com/hakkimizda" class="nav-link gp_lang_t_about ">Hakkımızda</a>
        </li>

        <li class="nav-item">
          <a id="etkinlikler_tab" href="https://www.goodparents.com/etkinlikler" class="nav-link gp_lang_t_activities ">Etkinlikler</a>
        </li>

        <li class="nav-item">
          <a id="etkinlik_merkezleri_tab" href="https://www.goodparents.com/etkinlik-merkezleri" class="nav-link text-nowrap gp_lang_t_activity_centers ">Etkinlik
            Merkezleri</a>
        </li>
        <li class="nav-item">
          <a id="iletisim_tab" href="https://www.goodparents.com/iletisim" class="nav-link gp_lang_t_contact ">İletişim</a>
        </li>
      </ul>


      <div class="text-nowrap mr-xl-auto">

        <a class="btn custom-navbar-button my-1 mr-3  d-none" href="/uyelik" role="button"><i class="fa fa-user mr-2"></i><span
                  class="gp_lang_t_sign_up navbarSmallText">Üye Ol</span>
          / <span class="gp_lang_t_sign_in navbarSmallText">Giriş Yap</span></a>

        <div class="dropdown">
          <button class="btn custom-navbar-button my-1 mr-3 dropdown-toggle" type="button" id="profileDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class=""><i class="fa fa-user mr-2"></i> Hamit Can Zor</span>
          </button>
          <div class="border-0 dropdown-menu navbar-profile-dropdown my-2" aria-labelledby="profileDropdown">
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/uyelik/dashboard" role="button"><i class="fa fa-user mr-2"></i>Profilim</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="#" role="button"><i class="fa fa-child mr-2"></i>Fatih Altaylı</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="#" role="button"><i class="fa fa-child mr-2"></i>Abdurrahman Cinli</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="#" role="button"><i class="fa fa-child mr-2"></i>Ömer Faruk Kıl</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/uyelik/bilgi" role="button"><i class="fa fa-cog mr-2"></i>Ayarlarım</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/uyelik/cikis" role="button"><i class="fa fa-sign-out mr-2"></i>Çıkış Yap</a>
          </div>
        </div>
      </div>

      <table class="my-1 navbar-text d-expanded-none">
        <tbody>
        <tr>
          <td><i class="fa fa-phone mr-1"></i></td>
          <td>
            <span class="navbarSmallText">+90 212 233 46 63</span><br>
            <span class="gp_lang_t_customer_services navbarSmallText">Müşteri Hizmetleri</span>
          </td>
        </tr>
        </tbody>
      </table>

      <form class="form-inline text-nowrap">
        <a class="custom-navbar-link d-none d-lg-block d-xl-block" href="https://www.instagram.com/goodparentscom/"><i class="fa fa-instagram"></i></a>
        <a class="custom-navbar-link d-none d-lg-block d-xl-block" href="https://www.facebook.com/goodparentsapp"><i class="fa fa-facebook"></i></a>
        <a class="custom-navbar-link d-none d-lg-block d-xl-block" href="#"><i class="fa fa-twitter"></i></a>
        <a class="custom-navbar-link d-none d-lg-block d-xl-block" href="#"><i class="fa fa-google-plus"></i></a>
      </form>

      <div class="text-nowrap ml-auto">
        <div class="dropdown">
          <button class="btn custom-navbar-button my-1 mr-3 dropdown-toggle" type="button" id="langDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span class="">Türkçe</span>
          </button>
          <div class="border-0 dropdown-menu navbar-profile-dropdown my-2" aria-labelledby="langDropdown">
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/tr/" role="button">Türkçe</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/en/" role="button">İngilizce</a>
            <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/ar/" role="button">Arapça</a>
          </div>
        </div>
      </div>

    </div>

    <div class="mobile-navbar d-block d-lg-none closed" id="mobile-navbar">
      <div class="d-flex flex-column py-3 px-0">
        <div class="w-100 d-flex flex-column align-items-center">
          <div class="text-nowrap">
            <a class="btn custom-navbar-button my-1 mr-3  d-none" href="/uyelik" role="button"><i class="fa fa-user mr-2"></i><span
                      class="gp_lang_t_sign_up navbarSmallText">Üye Ol</span>
              / <span class="gp_lang_t_sign_in navbarSmallText">Giriş Yap</span></a>

            <div class="dropdown">
              <button class="btn custom-navbar-button my-1 mr-3 dropdown-toggle" type="button" id="profileDropdownMobile" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class=""><i class="fa fa-user mr-2"></i> Hamit Can Zor</span>
              </button>
              <div class="border-0 dropdown-menu navbar-profile-dropdown my-2" aria-labelledby="profileDropdownMobile">
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/uyelik/dashboard" role="button"><i class="fa fa-user mr-2"></i>Profilim</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="#" role="button"><i class="fa fa-child mr-2"></i>Fatih Altaylı</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="#" role="button"><i class="fa fa-child mr-2"></i>Abdurrahman Cinli</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="#" role="button"><i class="fa fa-child mr-2"></i>Ömer Faruk Kıl</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/uyelik/bilgi" role="button"><i class="fa fa-cog mr-2"></i>Ayarlarım</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/uyelik/cikis" role="button"><i class="fa fa-sign-out mr-2"></i>Çıkış Yap</a>
              </div>
            </div>
          </div>
        </div>
        <div class="w-100 py-2">
          <div class="w-100">
            <a id="anasayfa_tab_mobile" href="https://www.goodparents.com/" class="d-block mobile-navbar-link px-5 py-2 text-center ">Anasayfa</a>
          </div>
          <div class="w-100">
            <a id="hakkimizda_tab_mobile" href="https://www.goodparents.com/hakkimizda" class="d-block  mobile-navbar-link px-5 py-2 text-center ">Hakkımızda</a>
          </div>
          <div class="w-100">
            <a id="etkinlikler_tab_mobile" href="https://www.goodparents.com/etkinlikler" class="d-block  mobile-navbar-link px-5 py-2 text-center ">Etkinlikler</a>
          </div>
          <div class="w-100">
            <a id="etkinlik_merkezleri_tab_mobile" href="https://www.goodparents.com/etkinlik-merkezleri" class="d-block  mobile-navbar-link px-5 py-2 text-center ">Etkinlik
              Merkezleri</a>
          </div>
          <div class="w-100">
            <a id="iletisim_tab_mobile" href="https://www.goodparents.com/iletisim" class="d-block  mobile-navbar-link px-5 py-2 text-center ">İletişim</a>
          </div>
        </div>
        <div class="w-100 d-flex flex-column align-items-center">
          <div class="py-2">
            <div class="dropdown">
              <button class="btn custom-navbar-button my-1 mr-3 dropdown-toggle" type="button" id="langDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class="">Türkçe</span>
              </button>
              <div class="border-0 dropdown-menu navbar-profile-dropdown my-2" aria-labelledby="langDropdown">
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/tr/" role="button">Türkçe</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/en/" role="button">İngilizce</a>
                <a class="btn btn-light w-100 gp-btn text-left d-block px-4 border-bottom" href="/ar/" role="button">Arapça</a>
              </div>
            </div>
          </div>
        </div>
        <div class="w-100 d-flex flex-column align-items-center">
          <table class="my-1 navbar-text d-expanded-none">
            <tbody>
            <tr>
              <td><i class="fa fa-phone mr-1"></i></td>
              <td>
                <span>+90 212 233 46 63</span><br>
                <span class="gp_lang_t_customer_services ">Müşteri Hizmetleri</span>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div class="w-100 d-flex flex-column align-items-center">
          <form class="form-inline text-nowrap py-3">
            <a class="mobile-navbar-link text-right px-3" href="https://www.instagram.com/goodparentscom/"><i class="fa fa-instagram"></i></a>
            <a class="mobile-navbar-link text-right px-3" href="https://www.facebook.com/goodparentsapp"><i class="fa fa-facebook"></i></a>
            <a class="mobile-navbar-link text-right px-3" href="#"><i class="fa fa-twitter"></i></a>
            <a class="mobile-navbar-link text-right px-3" href="#"><i class="fa fa-google-plus"></i></a>
          </form>
        </div>
      </div>
    </div>

  </div>

</nav>

<!--<div class="col-1 mx-auto d-none d-lg-block d-xl-block"><p class="text-center">|</p></div>-->

<!-- NAVIGATION END-->
<div style="position: fixed;max-width:350px;right: 10px;top:90px;z-index: 3000" id="alertContainer">

</div>
<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_4856308825c1d8b015607c9_33301952', 'body');
?>



<!-- MODAL RESPONSE START -->
<div class="modal fade" id="modalResponse" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content text-center">
      <div class="modal-header border-0 pb-0">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <form id="custom_form" action="">
        <input class="csrf" type="hidden" name="goodparents_csrf_token" value="4530acf8a716e16de92f9c97d991ec52">
        <div class="modal-body py-0">
          <i class="m_success fa fa-check-circle-o big-icon text-success d-block" aria-hidden="true"></i>
          <i class="m_fail fa fa-times-circle-o big-icon text-danger d-none" aria-hidden="true"></i>
          <i class="m_input fa fa-envelope big-icon text-info d-none" aria-hidden="true"></i>
          <i class="m_alert fa fa-exclamation-triangle big-icon  d-none text-secondary" aria-hidden="true"></i>
          <input type="text" class="form-control custom-text-input mx-auto d-none w-80 mt-3" id="custom_text_input" name="custom_text_input" placeholder="" />
          <p class="m_message custom-font-size-bigger mx-auto w-80 mt-1"></p>
        </div>
        <div class="modal-footer border-0 d-block text-center pb-4">
          <button type="button" class="btn btn-primary text-white font-weight-bold custom-font-size-bigger px-4" data-dismiss="modal">
            TAMAM
          </button>
        </div>
      </form>
    </div>
  </div>
</div>
<!-- MODAL RESPONSE END -->

<footer class="footer_widget4 dark pt_85  ">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <div class="contact_area text-center pb_50 py-5">
          <img class="footer_logo footer-goodparents-logo" src="/assets/images/logo.png" alt="Good Parents">
          <p class="my-4 text-white gp_lang_t_footer_logo_phrase ">Yeni blog yazılarımızla her zaman güncel kalın</p>
          <form id="blog_subscription_form" action="#" method="post" class="clearfix">
            <div class="input-group mb-3">
              <input id="blog_subscription_email" name="email" type="text" class="form-control custom-footer-input p-2 gp_lang_ph_enter_email " placeholder="E-posta adresinizi giriniz">
              <div class="input-group-append">
                <button id="blog_subscription_submit_button" class="btn custom-footer-button" type="button"><i class="fa fa-arrow-right text-primary"></i>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <!--/container-->

  <div class="footer_widget_area">
    <div class="container">
      <div class="row">

        <div class="col-xl-4 col-lg-4 col-md-12">
          <div class="single_widget widget4 text-center mb-5">
            <h2 class="widget_title text-uppercase gp_lang_t_contact_us ">Bize Ulaşın</h2>
            <div class="widget_txt mt-3">
              <p>Halaskargazi Mah. Rumeli Cad. No:1/23 Nişantaşı/İSTANBUL</p>
              <p>+90 212 233 46 63</p>
              <div class="social_links">
                <a href="https://www.instagram.com/goodparentscom/"><i class="fa fa-instagram fa-lg"></i></a>
                <a class="ml-4" href="https://www.facebook.com/goodparentsapp"><i class="fa fa-facebook fa-lg"></i></a>
                <a class="ml-4" href="#"><i class="fa fa-twitter fa-lg"></i></a>
                <a class="ml-4" href="#"><i class="fa fa-google-plus fa-lg"></i></a>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-4 col-lg-4 col-md-6">
          <div class="single_widget widget4">
            <div class="single_widget widget4 text-center mb-5">
              <h2 class="widget_title text-uppercase gp_lang_t_enterprise_membership ">Kurumsal Üyelik</h2>
              <p class="widget_txt mt-3 gp_lang_t_enterprise_membership_desc ">Kurumsal üye olarak kendi
                etkinliklerinizi oluşturabilirsiniz</p>
              <a class="gp-btn btn custom-navbar-button gp_lang_t_create_activity " href="https://www.goodparents.com/etkinlik-paneli" role="button">Etkinlik
                Oluştur</a>
            </div>
          </div>
        </div>

        <div class="col-xl-4 col-lg-4 col-md-6">
          <div class="single_widget widget4">
            <div class="single_widget widget4 text-center mb-5">
              <h2 class="widget_title text-uppercase gp_lang_t_site_map ">Site Haritası</h2>
              <div class="mt-3">
                <p class="mb-2">
                  <a href="https://www.goodparents.com/" class="text-uppercase gp_lang_t_home ">Anasayfa</a></p>
                <p class="mb-2">
                  <a href="https://www.goodparents.com/hakkimizda" class="text-uppercase gp_lang_t_about ">Hakkımızda</a>
                </p>
                <!-- <p class="mb-2"><a href="" class="text-uppercase gp_lang_t_activities"></a></p> -->
                <p class="mb-2">
                  <a href="https://www.goodparents.com/etkinlik-merkezleri" class="text-uppercase gp_lang_t_activity_centers ">Etkinlik
                    Merkezleri</a>
                </p>
                <p class="mb-2">
                  <a href="https://www.goodparents.com/iletisim" class="text-uppercase gp_lang_t_contact ">İletişim</a>
                </p>
              </div>
              <hr class="d-none d-lg-block d-xl-block" />
            </div>
          </div>
        </div>
        <!--/col-->
        <div class="footer-payment-image m-auto">
          <div class="mb-3">
            <img src="/assets/images/footer-payment.png">
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="last-footer">
    <p class="copyright text-center py-3 mb-0">
      <span class="gp_lang_t_copyright_phrase ">Copyright &#169; Tüm hakları saklıdır</span>
      <a class="font-weight-bold goodparents_link" href="" target="_blank">GOOD PARENTS</a></p>
  </div>
</footer>

<!-- FOOTER END -->
<?php echo '<script'; ?>
 src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/core/url_helpers.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/localization/languages/tr.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/localization/currencies/TRY.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/core/core.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/gp/gp-core.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/gp/gp-modal.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/gp/gp-popup.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/node_modules/popper.js/dist/umd/popper.min.js" crossorigin="anonymous"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/node_modules/bootstrap/dist/js/bootstrap.min.js" crossorigin="anonymous"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/jquery.form.min.js"><?php echo '</script'; ?>
>
<?php echo '<script'; ?>
 src="/assets/js/select/bootstrap-select.min.js"><?php echo '</script'; ?>
>

<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_14421242975c1d8b01560f50_64788219', 'js');
?>


</body>
</html><?php }
/* {block 'meta'} */
class Block_10268026555c1d8b0155f4c7_69409046 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'meta' => 
  array (
    0 => 'Block_10268026555c1d8b0155f4c7_69409046',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
}
}
/* {/block 'meta'} */
/* {block 'top_js'} */
class Block_17983007455c1d8b0155f944_95090152 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'top_js' => 
  array (
    0 => 'Block_17983007455c1d8b0155f944_95090152',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
}
}
/* {/block 'top_js'} */
/* {block 'css'} */
class Block_8656370275c1d8b0155fd94_10834086 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'css' => 
  array (
    0 => 'Block_8656370275c1d8b0155fd94_10834086',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php
}
}
/* {/block 'css'} */
/* {block 'body'} */
class Block_4856308825c1d8b015607c9_33301952 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'body' => 
  array (
    0 => 'Block_4856308825c1d8b015607c9_33301952',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

<?php
}
}
/* {/block 'body'} */
/* {block 'js'} */
class Block_14421242975c1d8b01560f50_64788219 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'js' => 
  array (
    0 => 'Block_14421242975c1d8b01560f50_64788219',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

<?php
}
}
/* {/block 'js'} */
}
