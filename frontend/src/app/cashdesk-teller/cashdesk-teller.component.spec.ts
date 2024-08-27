import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CashdeskTellerComponent } from './cashdesk-teller.component';

describe('CashdeskTellerComponent', () => {
  let component: CashdeskTellerComponent;
  let fixture: ComponentFixture<CashdeskTellerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CashdeskTellerComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CashdeskTellerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
