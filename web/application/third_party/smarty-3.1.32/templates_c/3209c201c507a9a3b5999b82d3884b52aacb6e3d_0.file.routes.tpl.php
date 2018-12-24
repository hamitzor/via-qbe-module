<?php
/* Smarty version 3.1.33, created on 2018-12-22 03:53:21
  from '/var/www/html/application/views/routes.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5c1d8b01554ff7_32147920',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '3209c201c507a9a3b5999b82d3884b52aacb6e3d' => 
    array (
      0 => '/var/www/html/application/views/routes.tpl',
      1 => 1545438627,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5c1d8b01554ff7_32147920 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_11845941445c1d8b01553800_58515161', "css");
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_5477142495c1d8b01554491_16606599', "js");
?>



<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_13983487105c1d8b015549b7_91797373', "body");
$_smarty_tpl->inheritance->endChild($_smarty_tpl, "layout.tpl");
}
/* {block "css"} */
class Block_11845941445c1d8b01553800_58515161 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'css' => 
  array (
    0 => 'Block_11845941445c1d8b01553800_58515161',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>


<?php
}
}
/* {/block "css"} */
/* {block "js"} */
class Block_5477142495c1d8b01554491_16606599 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'js' => 
  array (
    0 => 'Block_5477142495c1d8b01554491_16606599',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>


<?php
}
}
/* {/block "js"} */
/* {block "body"} */
class Block_13983487105c1d8b015549b7_91797373 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'body' => 
  array (
    0 => 'Block_13983487105c1d8b015549b7_91797373',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <div style="margin:40px">
    <div class="mb-2 text-center"><a href="/anasayfa" class="text-dark font-weight-regular" style="font-size: 1.5em">Anasayfa</a></div>
    <div class="mb-2 text-center"><a href="/giris" class="text-dark font-weight-regular" style="font-size: 1.5em">Giriş</a></div>
    <div class="mb-2 text-center"><a href="/arama_sonucu" class="text-dark font-weight-regular" style="font-size: 1.5em">Arama sonucu</a></div>
    <div class="mb-2 text-center"><a href="/iletisim" class="text-dark font-weight-regular" style="font-size: 1.5em">İletişim</a></div>
    <div class="mb-2 text-center"><a href="/hakkimizda" class="text-dark font-weight-regular" style="font-size: 1.5em">Hakkımızda</a></div>
    <div class="mb-2 text-center"><a href="/profil" class="text-dark font-weight-regular" style="font-size: 1.5em">Profil</a></div>
    <div class="mb-2 text-center"><a href="/profil_ayarlari" class="text-dark font-weight-regular" style="font-size: 1.5em">Profil Ayarları</a></div>
    <div class="mb-2 text-center"><a href="/merkezler" class="text-dark font-weight-regular" style="font-size: 1.5em">Merkezler</a></div>
    <div class="mb-2 text-center"><a href="/etkinlik_detayi" class="text-dark font-weight-regular" style="font-size: 1.5em">Etkinlik Detayı</a></div>
    <div class="mb-2 text-center"><a href="/odeme" class="text-dark font-weight-regular" style="font-size: 1.5em">Ödeme</a></div>
    <div class="mb-2 text-center"><a href="/odeme_basarili" class="text-dark font-weight-regular" style="font-size: 1.5em">Ödeme Başarılı</a></div>
    <div class="mb-2 text-center"><a href="/odeme_basarisiz" class="text-dark font-weight-regular" style="font-size: 1.5em">Ödeme Başarısız</a></div>
    <div class="mb-2 text-center"><a href="/parola_sifirla" class="text-dark font-weight-regular" style="font-size: 1.5em">Parola Sıfırla</a></div>
    <div class="mb-2 text-center"><a href="/etkinlikler" class="text-dark font-weight-regular" style="font-size: 1.5em">Etkinlikler</a></div>
    <div class="mb-2 text-center"><a href="/modal" class="text-dark font-weight-regular" style="font-size: 1.5em">Modal Demoları</a></div>
  </div>
<?php
}
}
/* {/block "body"} */
}
