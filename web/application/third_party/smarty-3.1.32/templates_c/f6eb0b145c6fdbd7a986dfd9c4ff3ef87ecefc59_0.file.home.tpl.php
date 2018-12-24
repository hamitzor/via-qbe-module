<?php
/* Smarty version 3.1.33, created on 2018-12-22 03:53:22
  from '/var/www/html/application/views/home.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5c1d8b02cd3820_68334238',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'f6eb0b145c6fdbd7a986dfd9c4ff3ef87ecefc59' => 
    array (
      0 => '/var/www/html/application/views/home.tpl',
      1 => 1545438627,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:partial/map.tpl' => 1,
    'file:partial/how-work.tpl' => 1,
    'file:partial/download-banner.tpl' => 1,
    'file:partial/activity-slider-card-hover.tpl' => 1,
  ),
),false)) {
function content_5c1d8b02cd3820_68334238 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_13507630355c1d8b02cc0c10_63759725', "css");
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_20176756385c1d8b02cc2794_95260498', "js");
?>




<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_79172505c1d8b02cc36f8_22931630', "body");
$_smarty_tpl->inheritance->endChild($_smarty_tpl, "layout.tpl");
}
/* {block "css"} */
class Block_13507630355c1d8b02cc0c10_63759725 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'css' => 
  array (
    0 => 'Block_13507630355c1d8b02cc0c10_63759725',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <link rel="stylesheet" href="/assets/css/bootstrap-checkbox.css">
  <link rel="stylesheet" href="/assets/css/map/jquery-ui.min.css">
  <link rel="stylesheet" href="/assets/css/map/map.css">
  <link rel="stylesheet" href="/assets/css/map/slick.css">
  <link rel="stylesheet" href="/assets/css/pages/home.css">
  <link rel="stylesheet" href="/assets/css/multidatespicker.css">
  <link rel="stylesheet" href="/assets/css/map/search.css">
  <link rel="stylesheet" href="/assets/css/calendar/bootstrap-datepicker3.min.css">
  <link rel="stylesheet" href="/assets/css/autocomplete/autocomplete.css">
  <link rel="stylesheet" href="/assets/css/gp/gp-slider.css">
  <link rel="stylesheet" href="/assets/css/gp/activity-slider.css">
  <link rel="stylesheet" href="/assets/css/gp/blog-slider.css">
<?php
}
}
/* {/block "css"} */
/* {block "js"} */
class Block_20176756385c1d8b02cc2794_95260498 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'js' => 
  array (
    0 => 'Block_20176756385c1d8b02cc2794_95260498',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php echo '<script'; ?>
 src="/assets/js/truncate/jquery.collapser.min.js" crossorigin="anonymous"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/jquery-ui.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/jquery.ui.touch-punch.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/slick.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/markerclusterer_packed.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/map.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/tether.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCjX5nB3IyhummFKjTUy3t164gA3kVbur8&callback=initMap" async defer><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/gp_slider.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/map/blog_slider.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/validation/jquery.validate.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/validation/localization/messages_tr.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/core/jquery-ui-radiocheckbox.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/calendar/bootstrap-datepicker.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/calendar/locales/bootstrap-datepicker.tr.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/calendar/locales/bootstrap-datepicker.ar.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/autocomplete/jquery.autocomplete.min.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/search-bar/search.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/gp/gp-slider.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
 src="/assets/js/pages/home.js"><?php echo '</script'; ?>
>
<?php
}
}
/* {/block "js"} */
/* {block "body"} */
class Block_79172505c1d8b02cc36f8_22931630 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'body' => 
  array (
    0 => 'Block_79172505c1d8b02cc36f8_22931630',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <div class="multiple-items d-none">
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
  </div>
  <div class="multiple-items d-none">
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
    <div>asdf</div>
  </div>
  <!-- MAIN CONTENT START -->
  <div class="d-none container-fluid">
    <div class="row">
      <div class="col-12">
        <div class="row">
          <div class="col-lg-6 p-0 home-featured-activity">
            <div id="featured-slider" class="carousel slide" data-ride="carousel" data-interval="3500">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img class="d-block w-100 activity_image_carousel" src="/assets/images/featured-activity.jpg" alt="">
                </div>
                <div class="carousel-item ">
                  <img class="d-block w-100 activity_image_carousel" src="/assets/images/featured-activity.jpg" alt="">
                </div>
                <div class="carousel-item ">
                  <img class="d-block w-100 activity_image_carousel" src="/assets/images/featured-activity.jpg" alt="">
                </div>
                <div class="carousel-item ">
                  <img class="d-block w-100 activity_image_carousel" src="/assets/images/featured-activity.jpg" alt="">
                </div>
                <div class="carousel-item ">
                  <img class="d-block w-100 activity_image_carousel" src="/assets/images/featured-activity.jpg" alt="">
                </div>
                <a class="carousel-control-prev" href="#featured-slider" role="button" data-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="sr-only gp_lang_t_previous ">Önceki</span>
                </a>
                <a class="carousel-control-next" href="#featured-slider" role="button" data-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="sr-only gp_lang_t_next ">Sonraki</span>
                </a>
              </div>
            </div>
          </div>
          <div class=" col-lg-6 p-0">
            <?php $_smarty_tpl->_subTemplateRender("file:partial/map.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- KATEGORİLER START-->
  <!-- KATEGORİLER END-->
  <div class="d-none container">
    <div class="row">
      <div class="col-md-10 mx-auto mt-2 text-center d-none">
        <a href="#"><img class="img-fluid" src="/assets/images/ad_example1.jpg" alt="Reklam Alanı"></a>
      </div>
    </div>
  </div>
  <div id="sliders" class="my-4">

    <?php
$_smarty_tpl->tpl_vars['z'] = new Smarty_Variable(null, $_smarty_tpl->isRenderingCache);$_smarty_tpl->tpl_vars['z']->step = 1;$_smarty_tpl->tpl_vars['z']->total = (int) ceil(($_smarty_tpl->tpl_vars['z']->step > 0 ? 2+1 - (0) : 0-(2)+1)/abs($_smarty_tpl->tpl_vars['z']->step));
if ($_smarty_tpl->tpl_vars['z']->total > 0) {
for ($_smarty_tpl->tpl_vars['z']->value = 0, $_smarty_tpl->tpl_vars['z']->iteration = 1;$_smarty_tpl->tpl_vars['z']->iteration <= $_smarty_tpl->tpl_vars['z']->total;$_smarty_tpl->tpl_vars['z']->value += $_smarty_tpl->tpl_vars['z']->step, $_smarty_tpl->tpl_vars['z']->iteration++) {
$_smarty_tpl->tpl_vars['z']->first = $_smarty_tpl->tpl_vars['z']->iteration === 1;$_smarty_tpl->tpl_vars['z']->last = $_smarty_tpl->tpl_vars['z']->iteration === $_smarty_tpl->tpl_vars['z']->total;?>
      <h3 class="mt-3 text-uppercase ml-5">Spor Etkinlikleri
        <span class="pl-1"><a href="https://www.goodparents.com/tr/spor" class="btn btn-outline-secondary font-weight-bold text-uppercase see-all-button ">Tümünü gör</a></span>
      </h3>
      <div class="activities-slider gp-slider-container mt-3 mb-5">
        <div class="gp-slider gp-slider-activity">
          <div class="gp-row">
            <?php
$_smarty_tpl->tpl_vars['i'] = new Smarty_Variable(null, $_smarty_tpl->isRenderingCache);$_smarty_tpl->tpl_vars['i']->step = 1;$_smarty_tpl->tpl_vars['i']->total = (int) ceil(($_smarty_tpl->tpl_vars['i']->step > 0 ? 20+1 - (0) : 0-(20)+1)/abs($_smarty_tpl->tpl_vars['i']->step));
if ($_smarty_tpl->tpl_vars['i']->total > 0) {
for ($_smarty_tpl->tpl_vars['i']->value = 0, $_smarty_tpl->tpl_vars['i']->iteration = 1;$_smarty_tpl->tpl_vars['i']->iteration <= $_smarty_tpl->tpl_vars['i']->total;$_smarty_tpl->tpl_vars['i']->value += $_smarty_tpl->tpl_vars['i']->step, $_smarty_tpl->tpl_vars['i']->iteration++) {
$_smarty_tpl->tpl_vars['i']->first = $_smarty_tpl->tpl_vars['i']->iteration === 1;$_smarty_tpl->tpl_vars['i']->last = $_smarty_tpl->tpl_vars['i']->iteration === $_smarty_tpl->tpl_vars['i']->total;?>
              <div class="gp-card slider-activity-card-container" style="width: 247.714px; height: 131.289px; margin-right: 5px;">
                <a href="" class="slider-activity-card lazy-background" data-background-image="/assets/images/test-activities/<?php echo $_smarty_tpl->tpl_vars['i']->value+12*$_smarty_tpl->tpl_vars['z']->value%5;?>
/1.jpg">
                  <div class="top-part">
                    <div class="left-part">Sarıyer</div>
                    <div class="right-part">450.00 ₺</div>
                  </div>
                  <div class="bottom-part">
                    <div class="left-part"><span>Uzun Etkinlik ismi - Test Test Test</span></div>
                    <div class="right-part"><img class="card-hour-icon" src="/assets/images/clock.png">
                      <div class="value">12-19</div>
                    </div>
                  </div>
                </a>
              </div>
            <?php }
}
?>
          </div>
        </div>
      </div>
    <?php }
}
?>
    <?php
$_smarty_tpl->tpl_vars['z'] = new Smarty_Variable(null, $_smarty_tpl->isRenderingCache);$_smarty_tpl->tpl_vars['z']->step = 1;$_smarty_tpl->tpl_vars['z']->total = (int) ceil(($_smarty_tpl->tpl_vars['z']->step > 0 ? -1+1 - (0) : 0-(-1)+1)/abs($_smarty_tpl->tpl_vars['z']->step));
if ($_smarty_tpl->tpl_vars['z']->total > 0) {
for ($_smarty_tpl->tpl_vars['z']->value = 0, $_smarty_tpl->tpl_vars['z']->iteration = 1;$_smarty_tpl->tpl_vars['z']->iteration <= $_smarty_tpl->tpl_vars['z']->total;$_smarty_tpl->tpl_vars['z']->value += $_smarty_tpl->tpl_vars['z']->step, $_smarty_tpl->tpl_vars['z']->iteration++) {
$_smarty_tpl->tpl_vars['z']->first = $_smarty_tpl->tpl_vars['z']->iteration === 1;$_smarty_tpl->tpl_vars['z']->last = $_smarty_tpl->tpl_vars['z']->iteration === $_smarty_tpl->tpl_vars['z']->total;?>
      <div class="gp-slider-container mt-5">
        <div class="gp-slider hidden-slider transparent-slider">
          <div class="gp-row">
            <?php
$_smarty_tpl->tpl_vars['i'] = new Smarty_Variable(null, $_smarty_tpl->isRenderingCache);$_smarty_tpl->tpl_vars['i']->step = 1;$_smarty_tpl->tpl_vars['i']->total = (int) ceil(($_smarty_tpl->tpl_vars['i']->step > 0 ? 20+1 - (0) : 0-(20)+1)/abs($_smarty_tpl->tpl_vars['i']->step));
if ($_smarty_tpl->tpl_vars['i']->total > 0) {
for ($_smarty_tpl->tpl_vars['i']->value = 0, $_smarty_tpl->tpl_vars['i']->iteration = 1;$_smarty_tpl->tpl_vars['i']->iteration <= $_smarty_tpl->tpl_vars['i']->total;$_smarty_tpl->tpl_vars['i']->value += $_smarty_tpl->tpl_vars['i']->step, $_smarty_tpl->tpl_vars['i']->iteration++) {
$_smarty_tpl->tpl_vars['i']->first = $_smarty_tpl->tpl_vars['i']->iteration === 1;$_smarty_tpl->tpl_vars['i']->last = $_smarty_tpl->tpl_vars['i']->iteration === $_smarty_tpl->tpl_vars['i']->total;?>
              <div class="gp-card">
                <div class="slider-activity-card lazy-background" data-background-image="https://www.goodparents.com/test_uploads/test-activities/<?php echo $_smarty_tpl->tpl_vars['i']->value+12*$_smarty_tpl->tpl_vars['z']->value%5;?>
/1.jpg">
                  <div class="top-part">
                    <div class="left-part">Sarıyer</div>
                    <div class="right-part">450.00 ₺</div>
                  </div>
                  <div class="bottom-part">
                    <div class="left-part"><span>Uzun Etkinlik ismi - Test Test Test</span></div>
                    <div class="right-part"><img class="card-hour-icon" src="/assets/images/clock.png">
                      <div class="value">12-19</div>
                    </div>
                  </div>
                </div>
              </div>
            <?php }
}
?>
          </div>
        </div>
      </div>
    <?php }
}
?>
  </div>
  <!--  YENİ EKLENEN HTML -->
  <div id="activity_sliders" class="container-fluid " style="margin-top: 250px  ;">
    <div class="row">
      <div class="col-12">
        <div class="col-12 px-1 px-sm-5">
                            </div>
      </div>
    </div>
  </div>
  <?php $_smarty_tpl->_subTemplateRender("file:partial/how-work.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
  <div class="container">
    <div class="row">
      <div class="col-10 mx-auto text-center mt-2 d-none">
        <a href="#"><img class="img-fluid" src="/assets/images/ad_example2.jpg" alt="Reklam Alanı"></a>
      </div>
    </div>
  </div>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12 bg-anasayfa-blog mt-4 pb-5">
        <div class="container">
          <div class="col-12 text-center">
            <img class="img-fluid" src="/assets/images/goodparents-blog.png" alt="">
            <p class="ustom-font-size-smaller gp_lang_t_blog_icon_desc ">Deneyimli anne bloggerlar hergün sizin için
              yazıyor.<br />Sorularınızı cevaplıyor ve pratik bilgiler veriyor.</p>
          </div>
        </div>

        <div class="container">
          <div class="row">
            <div class="col-12">
              <div class="blogs-slider gp-slider-container mt-5">
                <div data-role="blog-slider-left" class="blog-slider-arrow left">
                  <img src="/assets/images/blog-slider/slider-left.png">
                </div>
                <div data-role="blog-slider-right" class="blog-slider-arrow right">
                  <img src="/assets/images/blog-slider/slider-right.png">
                </div>
                <div class="gp-slider">
                  <div class="gp-row">
                    <?php
$_smarty_tpl->tpl_vars['i'] = new Smarty_Variable(null, $_smarty_tpl->isRenderingCache);$_smarty_tpl->tpl_vars['i']->step = 1;$_smarty_tpl->tpl_vars['i']->total = (int) ceil(($_smarty_tpl->tpl_vars['i']->step > 0 ? 10+1 - (0) : 0-(10)+1)/abs($_smarty_tpl->tpl_vars['i']->step));
if ($_smarty_tpl->tpl_vars['i']->total > 0) {
for ($_smarty_tpl->tpl_vars['i']->value = 0, $_smarty_tpl->tpl_vars['i']->iteration = 1;$_smarty_tpl->tpl_vars['i']->iteration <= $_smarty_tpl->tpl_vars['i']->total;$_smarty_tpl->tpl_vars['i']->value += $_smarty_tpl->tpl_vars['i']->step, $_smarty_tpl->tpl_vars['i']->iteration++) {
$_smarty_tpl->tpl_vars['i']->first = $_smarty_tpl->tpl_vars['i']->iteration === 1;$_smarty_tpl->tpl_vars['i']->last = $_smarty_tpl->tpl_vars['i']->iteration === $_smarty_tpl->tpl_vars['i']->total;?>
                      <div class="gp-card" style="width: 343.667px; height: 343.667px; margin-right: 20px;">
                        <a href="" class="blog-slider-card">
                          <img src="" class="blog-image lazy-background" data-background-image="/assets/images/test-blogs/<?php echo $_smarty_tpl->tpl_vars['i']->value;?>
/image.jpg">
                          <div class="blog-author">
                            <div class="left-part">
                              <img src="/assets/images/test-blogs/<?php echo $_smarty_tpl->tpl_vars['i']->value;?>
/author.jpg" class="author-image lazy-background">
                              <div class="author-name">Zeynep Gürbüz Gürbüz Gürbüz</div>
                            </div>
                            <div class="right-part">
                              <div class="friends"><img src="/assets/images/blog-friends.png" /><span class="font-weight-regular ml-1">5</span></div>
                              <div class="ml-1 ml-md-3 likes"><img src="/assets/images/blog-likes.png" /><span class="font-weight-regular ml-1">9</span></div>
                            </div>
                          </div>
                          <div class="hr"></div>
                          <div class="blog-title">
                            <div class="blog-title-text font-weight-regular">Çocuklarınızla Sokak etkinliklerini sıkılaştırın. Çünkü çocuklarınızla Sokak etkinliklerini sıkılaştırın Çocuklarınızla
                              Sokak etkinliklerini sıkılaştırın Çocuklarınızla Sokak etkinliklerini sıkılaştırın
                            </div>
                          </div>
                        </a>
                      </div>
                    <?php }
}
?>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>


      </div>

    </div>
  </div>
  <?php $_smarty_tpl->_subTemplateRender("file:partial/download-banner.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>

  <!-- A  ctivity slider'a tıklayınca açılan büyük card -->
  <?php $_smarty_tpl->_subTemplateRender("file:partial/activity-slider-card-hover.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
  <!-- MAIN CONTENT END -->

<?php
}
}
/* {/block "body"} */
}
