const membrosDiv = document.querySelector('.membros');

const alunos = [
  {
    name: 'Ana Letícia',
    matricula: '01600640'
  },
  {
    name: 'Carlos Frederico',
    matricula: '01285947'
  },
  {
    name: 'João Luis',
    matricula: '01510913'
  },
  {
    name: 'Lorena Mendes',
    matricula: '01528548'
  },
  {
    name: 'Pedro Vinicius',
    matricula: '01529186'
  }
]

const addMembers = () => {
  let mainDiv = membrosDiv;
  alunos.forEach((aluno) => {
    let div = document.createElement('div');
    div.classList.add('membro_card')
    let p1 = document.createElement('p');
    p1.classList.add('member_card_name')
    let p2 = document.createElement('p');
    p2.classList.add('member_card_matricula')

    p1.innerText = `Nome: ${aluno.name}`;
    p2.innerText = `Matricula: ${aluno.matricula}`;
    div.appendChild(p1);
    div.appendChild(p2);

    mainDiv.appendChild(div);
    console.log(mainDiv);
    return 0;
  })
  
}

addMembers()