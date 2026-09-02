<style>
.avatar-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 20px;
}
.alumni-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(90px, 1fr));
  gap: 10px;
  margin-top: 30px;
}
.avatar {
  text-align: center;
}
.avatar-grid img {
  width: 180px;
  height: 180px;
  border-radius: 20%;
  object-fit: cover;
}
.alumni-grid img {
  width: 90px;
  height: 90px;
  border-radius: 20%;
  object-fit: cover;
}
.avatar-grid .name {
  font-size: 18px;
}
.avatar-grid .institution {
  font-size: 12px;
}
.alumni-grid .name {
  font-size: 12px;
}
.alumni-grid .institution {
  font-size: 10px;
}

@media (max-width: 500px) {
  .avatar-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .avatar-grid img {
    width: 130px;
    height: 130px;
  }
}
</style>

<div class="avatar-grid">

  <div class="avatar">
    <img src="../img/edelen.jpg" alt="Auralee Edelen">
    <div class="name">Auralee Edelen</div>
    <div class="institution">SLAC</div>
  </div>

  <div class="avatar">
    <img src="../img/eichler.jpg" alt="Annika Eichler">
    <div class="name">Annika Eichler</div>
    <div class="institution">DESY</div>
  </div>

  <div class="avatar">
    <img src="../img/garcia.jpg" alt="Andrea Santamaria Garcia">
    <div class="name">Andrea Santamaria Garcia</div>
    <div class="institution">University of Liverpool</div>
  </div>
    
  <div class="avatar">
    <img src="../img/hofstaetter.jpg" alt="Georg Hoffstaetter">
    <div class="name">Georg Hoffstaetter</div>
    <div class="institution">Cornell</div>
   </div>
  
  <div class="avatar">
    <img src="../img/kain.jpg" alt="Verena Kain">
    <div class="name">Verena Kain</div>
    <div class="institution">CERN</div>
  </div>
  
  <div class="avatar">
    <img src="../img/maesaka.jpg" alt="Hirokazu Maesaka">
    <div class="name">Hirokazu Maesaka</div>
    <div class="institution">Spring-8</div>
   </div>
      
  <div class="avatar">
    <img src="../img/ratner.jpg" alt="Daniel Ratner">
    <div class="name">Daniel Ratner</div>
    <div class="institution">TJNAF</div>
  </div>
    
  <div class="avatar">
    <img src="../img/vay.jpg" alt="Jean-Luc Vay">
    <div class="name">Jean-Luc Vay</div>
    <div class="institution">LBNL</div>
  </div>

</div>

<h3>IOC Alumni</h3>
<div class="alumni-grid">

  <div class="avatar">
    <img src="../img/chu.jpg" alt="Paul Chu">
    <div class="name">Paul Chu</div>
    <div class="institution">NJU</div>
  </div>

  <div class="avatar">
    <img src="../img/brown.jpg" alt="Kevin Brown">
    <div class="name">Kevin Brown</div>
    <div class="institution">BNL</div>
  </div>

  <div class="avatar">
    <img src="../img/agapov.jpg" alt="Ilya Agapov">
    <div class="name">Ilya Agapov</div>
    <div class="institution">DESY</div>
  </div>

  <div class="avatar">
    <img src="../img/miceli.jpg" alt="Tia Miceli">
    <div class="name">Tia Miceli</div>
    <div class="institution">FNAL</div>
  </div>

  <div class="avatar">
    <img src="../img/adelmann.jpg" alt="Andreas Adelmann">
    <div class="name">Andreas Adelmann</div>
    <div class="institution">PSI</div>
  </div>

  <div class="avatar">
    <img src="../img/li.jpg" alt="Kevin Li">
    <div class="name">Kevin Li</div>
    <div class="institution">CERN</div>
  </div>

  <div class="avatar">
    <img src="../img/fukunishi.jpg" alt="Nobuhisa Fukunishi">
    <div class="name">Nobuhisa Fukunishi</div>
    <div class="institution">RIKEN</div>
  </div>

</div>
