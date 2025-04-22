import { Component, OnInit } from '@angular/core';
import { NgbModal, NgbModalRef } from '@ng-bootstrap/ng-bootstrap';
import { Movie, MoviesService } from '../services/movies.service';

@Component({
  selector: 'app-admin',
  imports: [],
  templateUrl: './admin.component.html',
  styleUrl: './admin.component.css',
})
export class AdminComponent implements OnInit {
  movies: Movie[] = [];
  busy = false;
  errorMsg = '';

  private modalRef?: NgbModalRef;
  constructor(
    private readonly svc: MoviesService,
    private modalService: NgbModal
  ) {}

  ngOnInit(): void {
    this.svc.getAllMovies().subscribe((x) => (this.movies = x));
  }

  delete(id: string, content: any) {
    this.svc.deleteMovie(id).subscribe({
      next: (_) => {
        this.ngOnInit();
      },
      error: (e) => {
        this.errorMsg = e.error.detail;
        this.modalService.open(content, {
          ariaLabelledBy: 'modal-title',
        });
      },
    });
  }
}
