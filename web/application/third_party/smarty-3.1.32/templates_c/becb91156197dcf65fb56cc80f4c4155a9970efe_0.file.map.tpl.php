<?php
/* Smarty version 3.1.33, created on 2018-12-22 03:53:22
  from '/var/www/html/application/views/partial/map.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5c1d8b02cd7f46_09509883',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'becb91156197dcf65fb56cc80f4c4155a9970efe' => 
    array (
      0 => '/var/www/html/application/views/partial/map.tpl',
      1 => 1545438627,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5c1d8b02cd7f46_09509883 (Smarty_Internal_Template $_smarty_tpl) {
?><!-- Search kısmı-->
<div id="mapSearchBar" class="map-search-bar-container mx-auto">
  <div class="map-search-bar">
    <div data-role="categorySelectorOpen" style="visibility:visible;opacity: 1" class="transition-opacity-250 category-selector-toggle">
      <button class="btn gp-btn btn-light font-weight-regular"><i class="fa fa-tags mr-1"></i> Kategoriler
      </button>
    </div>
    <div data-role="categorySelector" class="category-selector d-flex flex-row transition-opacity-250 align-self-start" style="visibility:hidden;opacity: 0">
      <div data-id="categories" class="category-list-container transition-opacity-250">
        <div class="px-1 py-1 list-title">Kategori</div>
        <div data-role="list" class="category-list">
          <div data-role="item" data-value="all" class="d-flex flex-row align-items-center item">
            <div class="d-flex flex-row align-items-center justify-content-center mx-2 icon-part">
              <img src="/assets/images/categories/all.png">
            </div>
            <div class="text-uppercase mr-4 name-part">Tümü</div>
          </div>
        </div>
      </div>
      <div data-id="subCategories" class="category-list-container transition-opacity-250 ml-2 align-self-start">
        <div class="px-1 py-1 list-title">Alt Kategori</div>
        <div data-role="list" class="category-list sub">
          <div data-role="item" data-value="all" class="d-flex flex-row align-items-center item sub active">
            <div class="text-uppercase mx-4 name-part sub">Tümü</div>
          </div>
        </div>
      </div>
      <div data-role="categorySelectorClose" class="close-button ml-2 align-self-start d-flex flex-row align-items-center justify-content-center">
        <i class="fa fa-close"></i>
      </div>
    </div>
    <div data-role="filter" data-id="filter" class="filter-extended container-fluid transition-opacity-250" style="visibility:hidden;opacity: 0">
      <div class="row py-0 px-2">
        <div class="col-12 px-1" data-role="calender-container">
          <div data-role="search-calender" class="d-flex flex-row justify-content-end mt-2">
          </div>
        </div>
        <div class="col-12 px-1">
          <div class="py-2">
            <div class="px-1 pb-2">
              <div data-role="labelContainer" data-id="ageRange" class="mb-2 d-flex flex-row justify-content-end font-weight-regular text-uppercase">
                          <span class="minMaxLabelContainer font-weight-bold">
                             <span data-role="minLabel">0 Aylık</span>
                          <span data-role="maxLabel">18 Yaş</span>
                          </span>
              </div>
              <div data-disabled="false" data-id="ageRange" data-role="range" data-min="0" data-max="30" data-multiplier="1" data-name="age"
                   class="setting-range-slider"></div>
            </div>
          </div>
          <div class="py-2">
            <div data-role="labelContainer" data-id="distanceRange" class="mb-2 d-flex flex-row justify-content-between align-items-center font-weight-regular">
              <div class="form-check abc-checkbox abc-checkbox-circle abc-checkbox-success px-1 py-1">
                <input id="cb2" data-role="rangeToggle" data-target="distanceRange" type="checkbox">
                <label class="form-check-label font-weight-regular text-white" style="font-size: 0.85em" for="cb2">Arama
                  mesafesi belirle</label>
              </div>
              <span class="minMaxLabelContainer font-weight-bold">
                            <span data-role="minLabel">0 KM</span> - <span data-role="maxLabel">100 KM</span>
                          </span>
            </div>
            <div class="px-1 pb-2 transition-padding-300">
              <div data-disabled="true" data-id="distanceRange" data-role="range" data-min="0" data-max="100" data-multiplier="1" data-name="distance" data-unit="KM"
                   class="setting-range-slider"></div>
            </div>
          </div>
          <div class="py-2">
            <div class="px-1 pb-2 transition-padding-300">
              <div data-role="labelContainer" data-id="priceRange" class="mb-2 d-flex flex-row justify-content-end font-weight-regular text-uppercase">
                          <span class="minMaxLabelContainer font-weight-bold">
                            <span data-role="minLabel">0 &#8378;</span><span data-role="maxLabel">5000 &#8378;</span>
                          </span>
              </div>
              <div data-disabled="false" data-id="priceRange" data-role="range" data-min="0" data-max="500" data-multiplier="10" data-name="price" data-unit="&#8378;"
                   class="setting-range-slider"></div>
            </div>
          </div>
          <div class="d-flex flex-row justify-content-end py-2">
            <button data-role="reset" type="button" class="btn btn-outline-light gp-btn font-weight-bold text-uppercase px-4 py-0 py-sm-1">
              Sıfırla
            </button>
            <button data-role="apply" type="button" class="btn btn-primary gp-btn font-weight-bold text-uppercase px-4 ml-2 py-0 py-sm-1">
              Uygula
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid">
      <div class="row p-1">
        <div class="col-6 col-sm-8 keyword-input-container">
          <input data-role="keyword" type="text" class="keyword-input" placeholder="Etkinlik ya da kurs ara...">
        </div>
        <div class="col-6 col-sm-4 filter ">
          <div class="row h-100 align-items-center">
            <div class="col-6 col-sm-7 col-md-6 p-0">
              <button data-role="filterToggle" data-target="filter" type="button" class="w-100 search-bar-button white-button">
                <img style="width:15px" class="mb-1" src="/assets/images/filter.png">
                <span data-role="value" class="mr-1">Filtrele</span>
              </button>
            </div>
            <div class="col-6 col-sm-5 col-md-6 p-0">
              <button data-role="submit" type="button" class="w-100 primary-button">
                <span data-role="value" class="mr-1 text-uppercase">Ara</span>
                <i class="fa fa-search" style="font-size: 1.1em"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="map-filter-alert green" style="display: none">
    <span class="content">Şuanda "<span class='text-uppercase font-weight-regular'></span>" kategorisi sonuçlarını incelemektesiniz</span><span class="ml-2 close-alert"><i
              class="fa fa-times-circle-o"></i></span>
  </div>
</div>
<div class="map-container">
  <!-- Zoom tool -->
  <div class="map-zoom-tool">
    <div class="zoom-slidercontainer">
      <div class="btn-zoom-plus"></div>
      <div class="btn-zoom-minus"></div>
      <div class="zoom-slider-left"></div>
      <div class="zoom-slider-right"></div>
      <input type="range" min="1" max="11" value="7" class="zoom-slider">
    </div>
  </div>
  <!-- Ana map -->
  <div id="map">
  </div>
</div><?php }
}
